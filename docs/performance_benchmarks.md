# Performance Benchmarks

This document outlines repeatable benchmarks for GPU acceleration on High Sierra using CUDA 10.2 + cuDNN 7.x with PyTorch 1.7.0.

## Benchmarks

1. GPU MatMul
   - Script: `examples/matmul_fp16_test.py`
   - Metric: GFLOPS, latency per 1024×1024 matmul in FP16 and FP32.

2. Transformer Inference (GPT-2)
   - Script: `examples/gpt2_streaming_generate.py` or `scripts/gpt2_benchmark.py`
   - Metric: tokens/sec on GPU vs CPU fallback.

3. CUDA Kernel Profiling
   - Script: `examples/profile_kernels.py`
   - Metric: kernel launch count, average kernel time, occupancy hints.

## Procedure

- Ensure WebDriver + CUDA + cuDNN configured.
- Set `TORCH_CUDA_ARCH_LIST=6.1`.
- Warm up kernels with a few iterations.
- Record results to `archive/test_outputs/` using `scripts/run_all_tests.sh`.

## Reporting

- Include hardware model, driver version, CUDA version, cuDNN version, PyTorch version.
- Use `scripts/system_probe.py --out environment/system_specs.json`.
- Attach SHA256 of wheel and CUDA libs from `archive/*`.