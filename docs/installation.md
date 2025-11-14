# Installation Guide (macOS High Sierra + CUDA 10.2)

## Requirements
- macOS 10.13.6 High Sierra
- NVIDIA Web Drivers (387.x – 387.10.10.10.40.x)
- CUDA Toolkit 10.2 (last macOS release)
- cuDNN 7.6.5
- Python 3.8 (Conda recommended)

## Install the Wheel

```
pip install wheel/torch-1.7.0a0-cp38-macosx_10_13_cuda102.whl
```

## Verify

```
python -c "import torch;print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"
```
