# Troubleshooting Guide

This guide addresses common pitfalls for macOS High Sierra (10.13) with NVIDIA WebDriver, CUDA 10.2, cuDNN 7.x, and PyTorch 1.7.0.

## WebDriver Issues

- Symptom: GPU not recognized, `torch.cuda.is_available() == False`.
  - Action: Ensure WebDriver version matches macOS build (e.g., 17G14042). Reinstall and reboot.
  - Check: `system_profiler SPDisplaysDataType` shows NVIDIA GPU and driver.

- Symptom: Kernel extension blocked.
  - Action: Disable or configure SIP to allow third-party kexts.
  - Check: `csrutil status`. Adjust from Recovery OS if necessary.

## CUDA Toolkit Problems

- `nvcc: command not found`
  - Action: Add `/usr/local/cuda/bin` to `PATH`.
  - Check: `nvcc --version` outputs 10.2.

- `libcudart.dylib` not found when importing PyTorch
  - Action: Add `/usr/local/cuda/lib` to `DYLD_LIBRARY_PATH`.
  - Verify: `otool -L $(python -c 'import torch, os; print(torch.__file__)')` shows CUDA links.

## cuDNN Issues

- `Symbol not found` or segfault in cuDNN ops
  - Action: Confirm cuDNN version matches CUDA 10.2.
  - Check: `strings /usr/local/cuda/lib/libcudnn.dylib | grep -i cudnnVersion`.

## sm_61 / arch targeting

- Performance is poor or kernels fail to launch
  - Action: Ensure `TORCH_CUDA_ARCH_LIST=6.1` for Pascal.
  - Rebuild: Use `-gencode arch=compute_61,code=sm_61` flags.

## nvcc Compilation Errors

- Undefined references to CUDA symbols
  - Likely ABI mismatch or missing `-lcudart` linkage; check `LIBRARY_PATH`.

- `unsupported macOS` messages
  - macOS 10.13 is supported by CUDA 10.2; ensure correct Xcode/Clang versions (Xcode 9.x toolchain).

## SIP (System Integrity Protection)

- Certain paths are protected; third-party kexts may not load.
  - Action: From Recovery, `csrutil enable --without kext` or similar mode compatible with your security policy.
  - Warning: Understand the security implications; restore SIP after validation if desired.

## Verification Scripts

- Run `scripts/verify_cuda.sh` for CUDA sanity checks.
- Run `scripts/system_probe.py` to dump comprehensive environment to JSON.
- Run `scripts/validate_whl.py` to check wheel compatibility and hashes.