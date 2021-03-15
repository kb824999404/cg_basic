# 线刷子直线生成算法
import cv2
import numpy as np
from utils import drawPixel
from bresenham import BresenhamLine,showImg

def BresenhamLine_line_brush(img,x0,y0,x1,y1,width,color):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dy)<=abs(dx):        #k∈[-1,1]，垂直线刷子
        for i in range(-width//2,width//2):
            img = BresenhamLine(img,x0,y0+i,x1,y1+i,color)
    else:                       #k∉[-1,1]，水平线刷子
        for i in range(-width//2,width//2): 
            img = BresenhamLine(img,x0+i,y0,x1+i,y1,color)
    return img




if __name__=='__main__':
    X , Y = 400,400
    #k∈[-1,1]
    img = np.zeros([X,Y],dtype=np.uint8)
    img = BresenhamLine_line_brush(img,0,0,300,200,19,255)
    showImg(img,"Line Brush","outputs/Line_Brush1.jpg")

    #k∉[-1,1]
    img = np.zeros([X,Y],dtype=np.uint8)
    img = BresenhamLine_line_brush(img,0,0,200,300,19,255)
    showImg(img,"Line Brush","outputs/Line_Brush2.jpg")

    #两线相接
    img = np.zeros([X,Y],dtype=np.uint8)
    img = BresenhamLine_line_brush(img,0,0,200,100,19,255)
    img = BresenhamLine_line_brush(img,200,100,300,400,20,255)
    showImg(img,"Line Brush","outputs/Line_Brush3.jpg")