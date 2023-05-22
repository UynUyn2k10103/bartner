import torch

print(torch.cuda.memory_summary(device='cuda', abbreviated=False))