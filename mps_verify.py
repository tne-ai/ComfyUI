#!/usr/bin/env python
import torch

if torch.backends.mps.is_available():
    print("mps is available")
    mps_device = torch.device("mps")
    x = torch.ones(1, device=mps_device)
    print(x)
else:
    print("mps is not available")
