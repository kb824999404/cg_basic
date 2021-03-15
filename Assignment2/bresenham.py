#Bresenham直线生成算法
import cv2
import numpy as np
from utils import drawPixel,showImg

def BresenhamLine(img,x0,y0,x1,y1,color):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dy)<=abs(dx):        #k∈[-1,1]
        # print("k in [-1,1]")
        e = -dx
        x = x0
        y = y0
        for i  in range(0,dx+1):
            drawPixel(img,x,y,color)
            x += 1
            e += 2*dy
            if e >= 0:
                y += 1
                e -= 2*dx
    else:
        # print("k not in [-1,1]")
        e = -dy
        x = x0
        y = y0
        for i  in range(0,dy+1):
            drawPixel(img,x,y,color)
            y += 1
            e += 2*dx
            if e >= 0:
                x += 1
                e -= 2*dy
    return img



if __name__=='__main__':
    X , Y = 400,400
    img = np.zeros([X,Y],dtype=np.uint8)
    img = BresenhamLine(img,0,0,300,400,255)

    showImg(img,"Bresenham")