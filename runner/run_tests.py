"""
Rust Test Runner — Flask HTTP server.

Receives user code, compiles with test file, runs tests,
returns only the first failure for anti-cheat pedagogy.
"""

import json
import os
import shutil
import subprocess
import tempfile
import uuid

from flask import Flask, request, jsonify

app = Flask(__name__)

BASE_EXERCISES_DIR = '/exercises'


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@app.route('/run', methods=['POST'])
def run_tests():
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'No JSON provided'}), 400

    code = data.get('code', '')
    day_number = data.get('day_number')
    exercise_id = data.get('exercise_id')
    timeout = data.get('timeout')

    if not code or not day_number or not exercise_id:
        return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400

    try:
        day_number = int(day_number)
    except (TypeError, ValueError):
        return jsonify({'status': 'error', 'message': 'Invalid day number'}), 400

    import re
    exercise_id = str(exercise_id)
    if not re.match(r'^[a-zA-Z0-9_\-]+$', exercise_id):
        return jsonify({'status': 'error', 'message': 'Invalid exercise ID format'}), 400

    if len(str(code)) > 50000:
        return jsonify({'status': 'error', 'message': 'Code payload too large.'}), 400

    try:
        timeout = int(timeout) if timeout is not None else 30
        timeout = min(max(timeout, 1), 60) # Clamp between 1 and 60 seconds
    except (TypeError, ValueError):
        timeout = 30

    # Locate test file
    test_file = os.path.join(
        EXERCISES_DIR,
        f'day{day_number}',
        exercise_id,
        f'test_{exercise_id}.rs'
    )

    if not os.path.exists(test_file):
        return jsonify({
            'status': 'error',
            'message': f'Test file not found for Day {day_number} / {exercise_id}'
        }), 404

    # Create isolated workspace
    workspace = os.path.join('/workspace', str(uuid.uuid4()))
    os.makedirs(workspace, exist_ok=True)

    try:
        return _compile_and_test(code, test_file, workspace, timeout)
    finally:
        shutil.rmtree(workspace, ignore_errors=True)


def _compile_and_test(code, test_file, workspace, timeout):
    """Compile user code + tests and run them."""
    # Read test file
    with open(test_file, 'r') as f:
        test_code = f.read()

    # Combine user code and test code into a single file
    combined = f"{code}\n\n#[cfg(test)]\nmod tests {{\n    use super::*;\n{test_code}\n}}\n"

    src_path = os.path.join(workspace, 'solution.rs')
    with open(src_path, 'w') as f:
        f.write(combined)

    # Compile
    binary_path = os.path.join(workspace, 'solution')
    compile_cmd = [
        'rustc',
        '--edition', '2021',
        '--test',
        '-o', binary_path,
        src_path,
    ]

    try:
        result = subprocess.run(
            compile_cmd,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        return jsonify({
            'status': 'error',
            'message': 'Compilation timed out (30s limit).'
        })

    if result.returncode != 0:
        error_msg = result.stderr.strip()
        # Clean up paths from error messages
        error_msg = error_msg.replace(workspace + '/', '')
        error_msg = error_msg.replace(src_path, 'solution.rs')
        return jsonify({
            'status': 'error',
            'message': f'Compilation Error:\n{error_msg}'
        })

    # Run tests
    run_timeout = timeout if timeout else 30

    try:
        result = subprocess.run(
            [binary_path, '--test-threads=1'],
            capture_output=True,
            text=True,
            timeout=run_timeout,
        )
    except subprocess.TimeoutExpired:
        return jsonify({
            'status': 'timeout',
            'message': f'Execution timed out ({run_timeout}s limit). '
                       f'Your solution may not be efficient enough. '
                       f'Consider optimizing your algorithm.'
        })

    stdout = result.stdout
    stderr = result.stderr

    if result.returncode == 0:
        return jsonify({
            'status': 'pass',
            'message': 'All tests passed.'
        })

    # Parse first failure
    first_failure = _extract_first_failure(stdout, stderr)
    return jsonify({
        'status': 'fail',
        'message': first_failure,
    })


def _extract_first_failure(stdout, stderr):
    """Extract only the first test failure from rustc test output."""
    lines = (stdout + '\n' + stderr).split('\n')

    failure_lines = []
    capturing = False
    found_failure = False

    for line in lines:
        if '---- ' in line and 'stdout ----' in line and not found_failure:
            capturing = True
            found_failure = True
            test_name = line.split('----')[1].strip().replace(' stdout ----', '')
            failure_lines.append(f"Test failed: {test_name}")
            continue

        if capturing:
            if line.startswith('---- ') or line.startswith('failures:') or line.strip() == '':
                if failure_lines:
                    break
            else:
                failure_lines.append(line)

    if failure_lines:
        return '\n'.join(failure_lines)

    # Fallback: return raw output (limited)
    combined = stdout + stderr
    if len(combined) > 500:
        combined = combined[:500] + '\n... (output truncated)'
    return combined if combined.strip() else 'Tests failed (unknown reason).'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=False)
