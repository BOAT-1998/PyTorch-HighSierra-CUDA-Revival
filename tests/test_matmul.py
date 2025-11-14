import torch
a = torch.randn(10000, 10000, device="cuda")
b = torch.randn(10000, 10000, device="cuda")
c = torch.mm(a, b)
torch.cuda.synchronize()
print("OK:", c.shape)
