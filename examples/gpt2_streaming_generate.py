#!/usr/bin/env python3
"""Streaming GPT-2 generation with CPU/GPU fallback.

Requires transformers; pinned versions may be necessary for PyTorch 1.7.0.
"""
import time

try:
    import torch
    from transformers import GPT2LMHeadModel, GPT2TokenizerFast
except Exception as e:
    print("Missing dependencies:", e)
    raise SystemExit(1)


def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Device:", device)
    tok = GPT2TokenizerFast.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2").to(device)
    prompt = "High Sierra CUDA revival: "
    input_ids = tok(prompt, return_tensors="pt").input_ids.to(device)
    t0 = time.time()
    out = model.generate(input_ids, max_length=64, do_sample=True, top_p=0.9)
    dt = time.time() - t0
    print("Time:", dt, "sec")
    print(tok.decode(out[0]))


if __name__ == "__main__":
    main()