
import rasterio
import numpy as np
from rasterio.enums import Resampling

def load_downsample(path, max_dim=256, bands=None):
    with rasterio.open(path) as src:
        if bands is None: bands = src.indexes
        w,h = src.width, src.height
        scale = max(1, max(w,h)/max_dim)
        out_w,out_h = int(w/scale), int(h/scale)
        data = src.read(bands, out_shape=(len(bands),out_h,out_w),
                        resampling=Resampling.bilinear)
    return data

def crop_center(data, win=128):
    _,H,W=data.shape
    cy,cx=H//2, W//2
    return data[:,cy-win//2:cy+win//2, cx-win//2:cx+win//2]
