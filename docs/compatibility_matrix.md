# Compatibility Matrix

This matrix lists GPUs known to work (Pascal, sm_61) on macOS 10.13 with WebDriver + CUDA 10.2 + cuDNN 7.x, and expected performance tiers.

## Supported GPUs (Pascal)

- GTX 1050 / 1050 Ti — Entry tier
- GTX 1060 (3GB/6GB) — Mid tier
- GTX 1070 — Upper mid tier
- GTX 1080 / 1080 Ti — High tier
- Titan X (Pascal) — High tier

## Likely Unsupported or Unstable

- Maxwell (sm_5x): may work with custom builds but not guaranteed.
- Turing/Volta/Ampere: no WebDriver on macOS; unsupported.

## Expected Performance Tiers

- Entry: small CNNs, basic matmul up to 1024², modest transformer inference.
- Mid: larger CNNs, transformer inference at practical speeds.
- High: large matmul, faster training/inference; memory capacity is key.

## Notes

- Ensure correct power and cooling; desktop GPUs perform better than mobile.
- PCIe bandwidth and display activity can affect kernel scheduling.