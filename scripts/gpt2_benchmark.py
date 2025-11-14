from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch, time

device = "cuda"
tok = GPT2Tokenizer.from_pretrained("gpt2-medium")
model = GPT2LMHeadModel.from_pretrained("gpt2-medium").to(device)

text = "Deep learning benchmark on High Sierra."
inp = tok.encode(text, return_tensors="pt").to(device)

t0 = time.time()
out = model.generate(inp, max_length=128)
t1 = time.time()

print("Output:", tok.decode(out[0]))
print("Time:", round(t1 - t0, 3), "s")
