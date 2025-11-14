# Build Notes (CUDA PyTorch for macOS High Sierra)

## Key Build Flags
```
USE_CUDA=ON
USE_CUDNN=ON
USE_MKLDNN=ON
USE_NNPACK=ON
USE_QNNPACK=ON
CUDA version: 10.2
cuDNN version: 7.6.5
GPU arch: sm_61 (Pascal)
```

## Compiler
```
Host compiler: Apple Clang (CommandLineTools)
NVCC: CUDA 10.2
```

## Notes
- Metal disabled
- NCCL disabled (not available on macOS)
- Distributed training disabled
- Python 3.8 required for C++ ABI compatibility
