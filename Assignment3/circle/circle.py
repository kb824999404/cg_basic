#圆弧生成算法
import cv2
import numpy as np
from utils import drawPixel_symmetric,showImg

#Bresenham圆弧生成算法
def BresenhamCircle(img,x0,y0,r,color):
    x=0;y=r
    d=3-2*r
    while x<=y:
        #八个对称点
        img=drawPixel_symmetric(img,x0,y0,x,y,color)
        if d<0:
            d+=4*x+7
        else:
            d+=4*(x-y)+11
            y-=1
        x+=1
    return img

#正负圆弧生成算法
def PositiveNegativeCircle(img,x0,y0,r,color):
    x=0;y=r
    f=0
    while x<=y:
        img=drawPixel_symmetric(img,x0,y0,x,y,color)
        if f<0:
            f+=2*x+1
            x+=1
        else:
            f+=1-2*y
            y-=1
    return img
    
#中点圆弧生成算法
def MiddleCircle(img,x0,y0,r,color):
    x=0;y=r
    d=1.25-r
    while x<=y:
        img=drawPixel_symmetric(img,x0,y0,x,y,color)
        if d<0:
            d+= 2*x+3
            x+=1
        else:
            d+= 2*(x-y)+5
            x+=1
            y-=1
    return img

if __name__=='__main__':
    X , Y = 800,800
    img = np.zeros([X,Y],dtype=np.uint8)
    img = MiddleCircle(img,400,400,200,255)

    showImg(img,"Circle")