from op import upfirdn2d
import torch

if __name__ == "__main__":
    print(f'Setting up the project')
    upfirdn2d(torch.zeros(4, 4, 4, 4), torch.zeros(4, 4))
    print(f'Upfirdn2d is working!')