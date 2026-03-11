/**
 * Piscine Rust — Client-side JavaScript
 * Handles code submission via AJAX, line numbers, and UI interactions.
 */

document.addEventListener('DOMContentLoaded', () => {
    initLineNumbers();
    initSubmitButton();
    initTabSupport();
});

/* --- Line Numbers --- */
function initLineNumbers() {
    const editor = document.getElementById('code-editor');
    const lineNumbers = document.getElementById('line-numbers');
    if (!editor || !lineNumbers) return;

    function updateLineNumbers() {
        const lines = editor.value.split('\n').length;
        let html = '';
        for (let i = 1; i <= Math.max(lines, 15); i++) {
            html += i + '\n';
        }
        lineNumbers.textContent = html.trimEnd();
    }

    // Sync scroll
    editor.addEventListener('scroll', () => {
        lineNumbers.scrollTop = editor.scrollTop;
    });

    editor.addEventListener('input', updateLineNumbers);
    updateLineNumbers();
}

/* --- Tab Support in Editor --- */
function initTabSupport() {
    const editor = document.getElementById('code-editor');
    if (!editor) return;

    editor.addEventListener('keydown', (e) => {
        if (e.key === 'Tab') {
            e.preventDefault();
            const start = editor.selectionStart;
            const end = editor.selectionEnd;
            editor.value = editor.value.substring(0, start) + '    ' + editor.value.substring(end);
            editor.selectionStart = editor.selectionEnd = start + 4;
            editor.dispatchEvent(new Event('input'));
        }
    });
}

/* --- Submit Code --- */
function initSubmitButton() {
    const btn = document.getElementById('submit-btn');
    if (!btn) return;

    btn.addEventListener('click', async () => {
        const editor = document.getElementById('code-editor');
        let code = '';
        if (window.editor) {
            code = window.editor.getValue().trim();
        } else {
            code = editor.value.trim();
        }

        if (!code) {
            showResult('error', 'Please write some code before submitting.');
            return;
        }

        // Show loading state
        const btnText = btn.querySelector('.btn-text');
        const btnLoader = btn.querySelector('.btn-loader');
        btn.disabled = true;
        btnText.style.display = 'none';
        btnLoader.style.display = 'inline-flex';

        try {
            const url = btn.dataset.url;
            const csrfToken = getCsrfToken();

            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({ code }),
            });

            const data = await response.json();
            showResult(data.status, data.message || data.error);
        } catch (err) {
            showResult('error', 'Network error. Please try again.');
        } finally {
            btn.disabled = false;
            btnText.style.display = 'inline';
            btnLoader.style.display = 'none';
        }
    });
}

/* --- Show Result --- */
function showResult(status, message) {
    const panel = document.getElementById('result-panel');
    const icon = document.getElementById('result-icon');
    const title = document.getElementById('result-title');
    const msg = document.getElementById('result-message');

    // Reset classes
    panel.className = 'result-panel';

    const statusConfig = {
        pass: {
            class: 'result-pass',
            icon: 'OK',
            title: 'All Tests Passed',
        },
        fail: {
            class: 'result-fail',
            icon: 'X',
            title: 'Test Failed',
        },
        error: {
            class: 'result-error',
            icon: '!',
            title: 'Error',
        },
        timeout: {
            class: 'result-timeout',
            icon: 'T',
            title: 'Timeout',
        },
    };

    const config = statusConfig[status] || statusConfig.error;
    panel.classList.add(config.class);
    icon.textContent = config.icon;
    title.textContent = config.title;
    msg.textContent = message;

    panel.style.display = 'block';

    // Scroll to result
    panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/* --- CSRF Token --- */
function getCsrfToken() {
    const cookie = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='));
    return cookie ? cookie.split('=')[1] : '';
}
