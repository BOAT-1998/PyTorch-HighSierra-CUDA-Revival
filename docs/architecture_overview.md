# Architecture Overview: CUDA → cuDNN → PyTorch → Python

This repository revives GPU acceleration on macOS High Sierra (10.13) with CUDA 10.2 and PyTorch 1.7.0. The stack is fragile and historically constrained; this document explains each layer, how they interoperate, and where common failure points occur.

## High-Level Stack

1. Hardware (NVIDIA GPU)
   - Typical: Pascal (sm_61) GPUs such as GTX 1050/1060/1070/1080, Titan X (Pascal).
   - macOS laptops/desktops with NVIDIA dGPU and WebDriver support.

2. macOS Kernel & WebDriver
   - Apple’s macOS 10.13 kernel with System Integrity Protection (SIP).
   - NVIDIA WebDriver provides user-space interfaces and kernel extensions for the GPU.
   - Version pinning is critical; GPU acceleration depends on correct driver–OS pairing.

3. CUDA Toolkit (10.2)
   - Compilers and runtime: `nvcc`, `libcudart`, `libcuda` stubs.
   - Developer headers and libraries located under `/usr/local/cuda`.
   - Device capability targeting: `-gencode arch=compute_61,code=sm_61` for Pascal.

4. cuDNN (7.x compatible with CUDA 10.2)
   - Deep-learning primitives for convolution, RNNs, batch norm, etc.
   - Installed typically into `/usr/local/cuda/lib` and `/usr/local/cuda/include`.
   - Must match CUDA version and ABI.

5. PyTorch (1.7.0)
   - Built against CUDA 10.2 and cuDNN 7.x with sm_61.
   - Provides high-level tensor ops, autograd, and neural network modules.
   - Links to CUDA runtime, cuDNN, and low-level kernels.

6. Python (3.8)
   - Orchestrates PyTorch modules and scripts.
   - Interacts with system paths and environment variables.

## Data Flow: A Simple op (GPU matmul)

1. Python calls `torch.matmul(A, B)`.
2. PyTorch dispatch selects CUDA kernel if `A` and `B` are CUDA tensors.
3. Kernel is enqueued on a CUDA stream via `libcudart`.
4. cuBLAS/cuDNN may be used (depending on op) to optimize execution.
5. WebDriver + kernel extensions mediate hardware execution.
6. Results are synchronized back to host when required.

## Key Environment Variables

- `CUDA_HOME` or `CUDA_PATH`: usually `/usr/local/cuda`.
- `DYLD_LIBRARY_PATH`: include CUDA and cuDNN dylib paths.
- `LIBRARY_PATH` / `CPATH`: include CUDA headers and libraries for compilation.
- `TORCH_CUDA_ARCH_LIST`: e.g., `6.1` for Pascal.
- `SIP_STATUS`: SIP must be configured to allow required kexts.

## Common Integration Points

- ABI compatibility: PyTorch must be compiled against the exact CUDA + cuDNN versions.
- Driver matching: WebDriver must match macOS build number (e.g., 17G65). Mismatch leads to GPU init failures.
- Device capability: Building with `sm_61` ensures kernels are compatible with Pascal GPUs.

## Failure Modes and Diagnostics

- ImportError for `libcudart.dylib`: path issues or missing CUDA.
- `nvcc` not found: CUDA toolkit not installed or not on `PATH`.
- cuDNN symbol mismatches: wrong cuDNN version.
- `torch.cuda.is_available() == False`: driver or toolkit not correctly detected.

## References

- NVIDIA CUDA Toolkit 10.2 documentation
- cuDNN 7.x release notes
- PyTorch 1.7.0 build docs (legacy)