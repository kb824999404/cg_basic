#球面片生成算法
import cv2
import numpy as np
from numpy.core.defchararray import mod
from utils import drawPixel_symmetric,showImg

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
 
def showVoxel(voxel):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
 
    ax.voxels(voxel, edgecolor="k")
    plt.show()

def inbound(x,y,z,r):
    print("X:{}\tY:{}\tZ:{}".format(x,y,z))
    return x>=0 and x<r and y>=0 and y<r and z>=0 and z<r

#Bresenham球面生成算法
def BresenhamSphere(model,x0,y0,z0,r,color):
    c=0 #截面半径
    z=r #z坐标
    d=3-2*r
    while c<=z:
        model=BresenhamCircle(model,x0,y0,c,z*color/r,z+z0)
        if d<0:
            d+=4*c+7
        else:
            d+=4*(c-z)+11
            z-=1
        c+=1
    return model

def BresenhamCircle(model,x0,y0,r,color,z):
    x=0;y=r
    d=3-2*r
    while x<=y:
        if inbound(x+x0,y+y0,z,r):
            model[x+x0,y+y0,z]=color
        if d<0:
            d+=4*x+7
        else:
            d+=4*(x-y)+11
            y-=1
        x+=1
    return model

if __name__=='__main__':
    global model
    R=20
    model = np.zeros([R,R,R],dtype=np.uint8)
    model = BresenhamSphere(model,0,0,0,R,255)
    print(model)
    showVoxel(model)