# Rebuild from Source (PyTorch 1.7.0 + CUDA 10.2 on macOS 10.13)

This guide documents a reproducible build process for the provided wheel. The process is historically constrained and may require legacy toolchains.

## Prerequisites

- macOS High Sierra (10.13), NVIDIA WebDriver matching OS build.
- CUDA Toolkit 10.2 installed at `/usr/local/cuda`.
- cuDNN 7.x for CUDA 10.2 placed under `/usr/local/cuda`.
- Xcode 9.x toolchain (Clang compatible with CUDA 10.2).
- CMake 3.16 or earlier recommended.
- Python 3.8 and pip.

## Environment Setup

```bash
export CUDA_HOME=/usr/local/cuda
export PATH="$CUDA_HOME/bin:$PATH"
export DYLD_LIBRARY_PATH="$CUDA_HOME/lib:${DYLD_LIBRARY_PATH}"
export TORCH_CUDA_ARCH_LIST=6.1
```

## Fetch Sources

- PyTorch 1.7.0 source
- Submodules: `third_party` libs

```bash
git clone --depth=1 --branch v1.7.0 https://github.com/pytorch/pytorch.git
cd pytorch
git submodule sync --recursive && git submodule update --init --recursive
```

## Configure Build Flags

- Ensure `CMAKE_PREFIX_PATH` includes Python site-packages and CUDA paths.
- Use `-gencode arch=compute_61,code=sm_61` in NVCC flags.

```bash
export CMAKE_PREFIX_PATH=$(python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')
export USE_CUDA=1 USE_NNPACK=0 USE_QNNPACK=0 USE_DISTRIBUTED=0
export CUDA_NVCC_EXECUTABLE=$CUDA_HOME/bin/nvcc
export EXTRA_CUDA_CFLAGS="-Xcompiler -fno-strict-aliasing -gencode arch=compute_61,code=sm_61"
```

## Build

```bash
python setup.py bdist_wheel
```

Artifacts are produced under `dist/`. Record SHA256 to `wheel/SHA256SUMS`.

## Notes

- Some ops may need to be disabled on macOS due to driver constraints.
- Ensure SIP configuration allows required kexts.
- Keep detailed logs under `/archive/build_logs/`.