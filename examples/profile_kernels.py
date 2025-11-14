#!/usr/bin/env python3
import time
import torch


def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    x = torch.randn(1, 3, 224, 224, device=device)
    conv = torch.nn.Conv2d(3, 16, 3).to(device)
    # warmup
    for _ in range(10):
        conv(x)
    torch.cuda.synchronize() if device == "cuda" else None
    t0 = time.time()
    for _ in range(100):
        conv(x)
    torch.cuda.synchronize() if device == "cuda" else None
    print("Elapsed:", time.time() - t0)


if __name__ == "__main__":
    main()