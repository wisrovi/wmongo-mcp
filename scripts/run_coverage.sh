#!/usr/bin/env bash
set -e

echo "=== Running wmongo-mcp pytest suite ==="
PYTHONPATH=src pytest tests/
