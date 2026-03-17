FROM rust:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /runner

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir flask==3.0.0

COPY run_tests.py .

RUN mkdir -p /exercises /workspace

EXPOSE 8001

CMD ["python3", "run_tests.py"]
