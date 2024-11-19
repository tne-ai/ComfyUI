# Detailed Mac installation instructions

This uses poetry not conda or pip3.

First you need basic tools:

- Apple Pytorch [installation](https://developer.apple.com/metal/pytorch/)
- PyTorch compile from [source](https://github.com/pytorch/pytorch#from-source)
  is optional, you should pip install
- Verify MPS is running with test program

```sh
brew install uv xcode python@3.12 asdf direnv
uv init
uv pip install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
./mps_verify.py
uv pip install -r requirements.txt
```

Where mps_verify.py is:

```python
import torch
if torch.backends.mps.is_available():
  mps_device = torch.device("mps")
  x = torch.ones(1, device=mps_device)
  print(f"mps available: x={x}")
```

## UV build environment and asdf and direnv

There is a .direnv in the comfyui that switches you the the comfy venv
automatically.

## Build Comfy

First you need to make sure the big files are:

1. SD Checkpoints in `models/checkpoints`
1. VAE in `models/vae`

You might want to put this in a Thunderbolt Drive as they get big.
