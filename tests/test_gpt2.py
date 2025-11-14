from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
device = "cuda"

tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
model = GPT2LMHeadModel.from_pretrained("gpt2-medium").to(device)

inp = tokenizer.encode("hello world", return_tensors="pt").to(device)
out = model.generate(inp, max_length=50)

print(tokenizer.decode(out[0]))
