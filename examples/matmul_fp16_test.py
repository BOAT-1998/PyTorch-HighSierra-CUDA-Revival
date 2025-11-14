#!/usr/bin/env python3
import time
import torch


def bench(n=1024, dtype=torch.float16, device=None):
    device = device or ("cuda" if torch.cuda.is_available() else "cpu")
    a = torch.randn((n, n), dtype=dtype, device=device)
    b = torch.randn((n, n), dtype=dtype, device=device)
    # warmup
    for _ in range(10):
        torch.matmul(a, b)
    torch.cuda.synchronize() if device == "cuda" else None
    t0 = time.time()
    for _ in range(50):
        torch.matmul(a, b)
    torch.cuda.synchronize() if device == "cuda" else None
    dt = time.time() - t0
    print(f"{device} {dtype} matmul {n}x{n} avg {(dt/50):.6f}s")


if __name__ == "__main__":
    bench()