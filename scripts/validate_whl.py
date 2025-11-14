#!/usr/bin/env python3
"""Validate wheel integrity, ABI tags, and optional CUDA availability.

This script inspects the wheel under ./wheel and emits a JSON report with:
- SHA256 of the wheel file
- Detected wheel tags (platform, python)
- Torch import and cuda availability (if torch installed)
"""
import hashlib
import json
import os
import sys
import zipfile
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def wheel_report(wheel_path: Path) -> dict:
    report = {"wheel": str(wheel_path), "exists": wheel_path.exists()}
    if not wheel_path.exists():
        return report

    report["sha256"] = sha256(wheel_path)

    with zipfile.ZipFile(wheel_path, "r") as z:
        # Read WHEEL and METADATA for tags
        try:
            wheel_txt = z.read("*.dist-info/WHEEL")
        except KeyError:
            # find the dist-info directory
            distinfo = [n for n in z.namelist() if n.endswith(".dist-info/WHEEL")]
            wheel_txt = z.read(distinfo[0]) if distinfo else b""

        try:
            meta_txt = z.read("*.dist-info/METADATA")
        except KeyError:
            distmeta = [n for n in z.namelist() if n.endswith(".dist-info/METADATA")]
            meta_txt = z.read(distmeta[0]) if distmeta else b""

    report["wheel_tags"] = {}
    wt = wheel_txt.decode("utf-8", errors="ignore")
    for line in wt.splitlines():
        if line.startswith("Tag:"):
            report["wheel_tags"].setdefault("tags", []).append(line.split("Tag:", 1)[1].strip())

    # Optional torch import
    try:
        import torch

        report["torch"] = {
            "version": torch.__version__,
            "cuda_available": bool(torch.cuda.is_available()),
        }
    except Exception as e:
        report["torch_error"] = str(e)

    return report


def main():
    wheel_dir = Path("wheel")
    wheels = list(wheel_dir.glob("*.whl"))
    if not wheels:
        print(json.dumps({"error": "no_wheel_found", "dir": str(wheel_dir)}, indent=2))
        sys.exit(0)
    report = wheel_report(wheels[0])
    out = Path("archive/wheel_hashes.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"{Path(report['wheel']).name} {report.get('sha256','')}\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()