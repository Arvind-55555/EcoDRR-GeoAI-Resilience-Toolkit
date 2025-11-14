
import numpy as np

def extract_patches(image, ps=32):
    b,H,W=image.shape
    out=[]
    for y in range(0,H-ps+1,ps):
        for x in range(0,W-ps+1,ps):
            out.append(image[:,y:y+ps,x:x+ps])
    return np.stack(out,0)
