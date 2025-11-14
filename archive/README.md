# Archive Contents

This folder preserves build logs, flags, caches, hashes, and test outputs for long-term reproducibility.

## Layout

- `build_logs/` — full build output logs
- `nvcc_flags.txt` — NVCC flags used to build CUDA-dependent targets
- `cmake_cache.txt` — CMake configuration cache
- `wheel_hashes.txt` — SHA256 of built wheels
- `cuda_libs_sha256.txt` — SHA256 of CUDA libraries used
- `test_outputs/` — terminal outputs from tests and benchmarks