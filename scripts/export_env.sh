#!/usr/bin/env bash
set -euo pipefail

# Export key environment info to JSON and YAML for reproducibility.
# Usage: scripts/export_env.sh [output_dir]

OUT_DIR=${1:-environment}
mkdir -p "$OUT_DIR"

timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

cuda_home=${CUDA_HOME:-/usr/local/cuda}
python_ver=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')
pytorch_ver=$(python3 -c 'import importlib, json; \
    m=importlib.util.find_spec("torch"); \
    print(__import__("torch").__version__) if m else print("not_installed")')
cuda_ver=$(cat "$cuda_home/version.txt" 2>/dev/null || echo "unknown")
cudnn_ver=$(strings "$cuda_home/lib/libcudnn.dylib" 2>/dev/null | grep -i cudnnVersion | head -n1 | awk '{print $NF}')

cat > "$OUT_DIR/pip_environment.json" <<JSON
{
  "timestamp": "$timestamp",
  "python_version": "$python_ver",
  "pytorch_version": "$pytorch_ver",
  "cuda_home": "$cuda_home",
  "cuda_version": "$cuda_ver",
  "cudnn_version": "${cudnn_ver:-unknown}",
  "env": {
    "PATH": "${PATH}",
    "DYLD_LIBRARY_PATH": "${DYLD_LIBRARY_PATH:-}",
    "TORCH_CUDA_ARCH_LIST": "${TORCH_CUDA_ARCH_LIST:-}",
    "CUDA_VISIBLE_DEVICES": "${CUDA_VISIBLE_DEVICES:-}"
  }
}
JSON

cat > "$OUT_DIR/environment.yml" <<YAML
timestamp: "$timestamp"
python_version: "$python_ver"
pytorch_version: "$pytorch_ver"
cuda_home: "$cuda_home"
cuda_version: "$cuda_ver"
cudnn_version: "${cudnn_ver:-unknown}"
env:
  PATH: "${PATH}"
  DYLD_LIBRARY_PATH: "${DYLD_LIBRARY_PATH:-}"
  TORCH_CUDA_ARCH_LIST: "${TORCH_CUDA_ARCH_LIST:-}"
  CUDA_VISIBLE_DEVICES: "${CUDA_VISIBLE_DEVICES:-}"
YAML

echo "Wrote $OUT_DIR/pip_environment.json and $OUT_DIR/environment.yml"