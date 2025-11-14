#!/usr/bin/env bash
set -euo pipefail

# Run all tests and capture outputs to archive/test_outputs.

ROOT_DIR=$(cd "$(dirname "$0")/.." && pwd)
mkdir -p "$ROOT_DIR/archive/test_outputs"

timestamp=$(date -u +"%Y%m%d-%H%M%S")
outfile="$ROOT_DIR/archive/test_outputs/test_run_${timestamp}.txt"

echo "Running tests..."
pytest -q "$ROOT_DIR/tests" | tee "$outfile"
echo "Test output saved to $outfile"