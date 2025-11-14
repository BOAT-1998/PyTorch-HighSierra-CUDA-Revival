#!/usr/bin/env python3
import json
import torch


def main():
    info = {"cuda_available": torch.cuda.is_available()}
    if torch.cuda.is_available():
        info.update(
            {
                "device_name": torch.cuda.get_device_name(0),
                "memory_allocated": int(torch.cuda.memory_allocated(0)),
                "memory_reserved": int(torch.cuda.memory_reserved(0)),
            }
        )
    print(json.dumps(info, indent=2))


if __name__ == "__main__":
    main()