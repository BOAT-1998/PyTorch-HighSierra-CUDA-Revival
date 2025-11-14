#!/usr/bin/env python3
import json
import os
import platform
import subprocess
from pathlib import Path


def sh(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        return e.output


def read_file(path):
    p = Path(path)
    if p.exists():
        try:
            return p.read_text(errors="ignore")
        except Exception:
            return None
    return None


def probe():
    data = {
        "timestamp": sh("date -u +%Y-%m-%dT%H:%M:%SZ").strip(),
        "system": {
            "os": platform.system(),
            "os_release": platform.release(),
            "mac_ver": platform.mac_ver()[0],
            "machine": platform.machine(),
        },
        "python": {
            "version": platform.python_version(),
        },
        "torch": {},
        "cuda": {},
        "cudnn": {},
        "gpu": {},
    }

    # PyTorch
    try:
        import torch

        data["torch"]["version"] = torch.__version__
        data["torch"]["cuda_available"] = bool(torch.cuda.is_available())
        data["torch"]["cuda_device_count"] = torch.cuda.device_count() if torch.cuda.is_available() else 0
        if torch.cuda.is_available():
            data["torch"]["device_name"] = torch.cuda.get_device_name(0)
    except Exception as e:
        data["torch"]["error"] = str(e)

    # CUDA toolkit
    data["cuda"]["home"] = os.environ.get("CUDA_HOME", "/usr/local/cuda")
    data["cuda"]["nvcc_version"] = sh("nvcc --version")
    data["cuda"]["version_txt"] = read_file(os.path.join(data["cuda"]["home"], "version.txt"))

    # cuDNN
    cudnn_header = os.path.join(data["cuda"]["home"], "include", "cudnn.h")
    cudnn_lib = os.path.join(data["cuda"]["home"], "lib", "libcudnn.dylib")
    header = read_file(cudnn_header)
    data["cudnn"]["header_present"] = bool(header)
    data["cudnn"]["lib_present"] = Path(cudnn_lib).exists()
    if header:
        # Parse version from header if available
        import re

        m = re.search(r"#define\s+CUDNN_MAJOR\s+(\d+).*#define\s+CUDNN_MINOR\s+(\d+).*#define\s+CUDNN_PATCHLEVEL\s+(\d+)", header, re.S)
        if m:
            data["cudnn"]["version"] = ".".join(m.groups())

    # GPU via system_profiler (macOS)
    sp = sh("system_profiler SPDisplaysDataType")
    data["gpu"]["system_profiler"] = sp

    return data


def main():
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="environment/system_specs.json")
    args = ap.parse_args()

    report = probe()
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2))
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()