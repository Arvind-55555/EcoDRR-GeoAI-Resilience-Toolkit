
import torch.nn as nn
import torch

class TinyUNet(nn.Module):
    def __init__(self, inc, cls):
        super().__init__()
        self.e1=nn.Sequential(nn.Conv2d(inc,16,3,padding=1),nn.ReLU(),
                              nn.Conv2d(16,16,3,padding=1),nn.ReLU())
        self.p=nn.MaxPool2d(2)
        self.e2=nn.Sequential(nn.Conv2d(16,32,3,padding=1),nn.ReLU(),
                              nn.Conv2d(32,32,3,padding=1),nn.ReLU())
        self.u=nn.ConvTranspose2d(32,16,2,stride=2)
        self.d1=nn.Sequential(nn.Conv2d(32,16,3,padding=1),nn.ReLU(),
                              nn.Conv2d(16,16,3,padding=1),nn.ReLU())
        self.out=nn.Conv2d(16,cls,1)

    def forward(self,x):
        e1=self.e1(x); e2=self.e2(self.p(e1))
        u=self.u(e2)
        d=self.d1(torch.cat([u,e1],1))
        return self.out(d)
