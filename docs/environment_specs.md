## 🔧 Verified Test Environment

```
$ nvcc --version
Cuda compilation tools, release 10.2, V10.2.89

$ python --version
Python 3.8.20

$ conda --version
conda 23.5.2

$ python -m pip --version
pip 24.2 (Python 3.8)
```

This wheel was built & validated inside the environment above. Any system matching these versions (or close variants) will work.

---
# 📦 Python Package Environment — Verified Working Set  
### *PyTorch CUDA 10.2 Build on macOS High Sierra (careunix)*

This document contains the **exact Python package list** used during the successful compilation of:

- PyTorch **1.7.0a0** (custom CUDA build)
- CUDA **10.2**
- cuDNN **7.6.5**
- Python **3.8.20**
- Conda **23.5.2**

Environment name: **gpt2env**  
Primary developer: **careunix**

These versions are confirmed **100% compatible** and form a *fully reproducible build environment*.

---

## 📌 Export Your Own List  
You can generate the same format with:

```bash
python -m pip list --format=json > pip_environment.json
```

---

## ✔ Verified Working Package Set  
*(Direct JSON output from careunix’s functional build environment)*

```json
[
  {"name": "accelerate", "version": "1.0.1"},
  {"name": "autocommand", "version": "2.2.2"},
  {"name": "backports.tarfile", "version": "1.2.0"},
  {"name": "Brotli", "version": "1.0.9"},
  {"name": "certifi", "version": "2024.8.30"},
  {"name": "cffi", "version": "1.17.1"},
  {"name": "charset-normalizer", "version": "3.3.2"},
  {"name": "click", "version": "8.1.8"},
  {"name": "filelock", "version": "3.16.1"},
  {"name": "future", "version": "0.18.3"},
  {"name": "huggingface-hub", "version": "0.0.12"},
  {"name": "idna", "version": "3.7"},
  {"name": "importlib_metadata", "version": "8.0.0"},
  {"name": "importlib_resources", "version": "6.4.0"},
  {"name": "inflect", "version": "7.3.1"},
  {"name": "jaraco.collections", "version": "5.1.0"},
  {"name": "jaraco.context", "version": "5.3.0"},
  {"name": "jaraco.functools", "version": "4.0.1"},
  {"name": "jaraco.text", "version": "3.12.1"},
  {"name": "joblib", "version": "1.4.2"},
  {"name": "mkl-fft", "version": "1.3.8"},
  {"name": "mkl-random", "version": "1.2.4"},
  {"name": "mkl-service", "version": "2.4.0"},
  {"name": "more-itertools", "version": "10.3.0"},
  {"name": "numpy", "version": "1.23.5"},
  {"name": "packaging", "version": "25.0"},
  {"name": "pip", "version": "24.2"},
  {"name": "platformdirs", "version": "4.2.2"},
  {"name": "pycparser", "version": "2.21"},
  {"name": "PySocks", "version": "1.7.1"},
  {"name": "PyYAML", "version": "6.0.2"},
  {"name": "regex", "version": "2024.11.6"},
  {"name": "requests", "version": "2.32.3"},
  {"name": "sacremoses", "version": "0.1.1"},
  {"name": "setuptools", "version": "75.1.0"},
  {"name": "six", "version": "1.16.0"},
  {"name": "tokenizers", "version": "0.10.3"},
  {"name": "tomli", "version": "2.0.1"},
  {
    "name": "torch",
    "version": "1.7.0a0",
    "editable_project_location": "/Users/careunix/pytorch"
  },
  {"name": "tqdm", "version": "4.67.1"},
  {"name": "transformers", "version": "4.8.2"},
  {"name": "typeguard", "version": "4.3.0"},
  {"name": "typing_extensions", "version": "4.11.0"},
  {"name": "urllib3", "version": "2.2.3"},
  {"name": "wheel", "version": "0.44.0"},
  {"name": "zipp", "version": "3.19.2"}
]
```

---

## 🏁 Notes
- This list ensures your build can be identically recreated.
- This file is part of the *CUDA Revival Project* led by **careunix**.
- If you fork the main repo, include this file for scientific reproducibility.
