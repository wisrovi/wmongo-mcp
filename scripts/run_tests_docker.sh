#!/usr/bin/env bash
set -e

echo "=== Running wmongo-mcp tests inside Docker container ==="
docker run --rm -v "$(pwd):/app" -w /app python:3.11-slim bash -c "
    pip install -e .[dev] &&
    PYTHONPATH=src pytest tests/
"
