# 方形直线生成算法
import cv2
import numpy as np
from utils import drawPixel
from bresenham import BresenhamLine,showImg

def BresenhamLine_square_brush(img,x0,y0,x1,y1,width,color):
    dx = x1 - x0
    dy = y1 - y0
    for i in range(-width//2,width//2):
        for j in range(-width//2,width//2):
            img = BresenhamLine(img,x0+i,y0+j,x1+i,y1+j,color)
    return img



if __name__=='__main__':
    X , Y = 400,400
    #k∈[-1,1]
    img = np.zeros([X,Y],dtype=np.uint8)
    img = BresenhamLine_square_brush(img,100,100,350,300,19,255)
    showImg(img,"Square Brush","outputs/Square_Brush1.jpg")

    #k∉[-1,1]
    img = np.zeros([X,Y],dtype=np.uint8)
    img = BresenhamLine_square_brush(img,100,100,300,350,19,255)
    showImg(img,"Square Brush","outputs/Square_Brush2.jpg")

    #两线相接
    img = np.zeros([X,Y],dtype=np.uint8)
    img = BresenhamLine_square_brush(img,0,0,200,100,19,255)
    img = BresenhamLine_square_brush(img,200,100,300,400,19,255)
    showImg(img,"Square Brush","outputs/Square_Brush3.jpg")