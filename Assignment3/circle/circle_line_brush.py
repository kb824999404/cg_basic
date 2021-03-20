#线刷子圆弧生成算法
import cv2
import numpy as np
from utils import drawPixel_symmetric,showImg
import datetime

def BresenhamCircle_line_brush(img,x0,y0,r,width,color):
    x=0;y=r
    d=3-2*r
    while x<=y:
        for w in range(-width//2,width//2):
        #八个对称点
            img=drawPixel_symmetric(img,x0,y0,x,y+w,color)
        if d<0:
            d+=4*x+7
        else:
            d+=4*(x-y)+11
            y-=1
        x+=1
    return img

if __name__=='__main__':
    X , Y = 800,800

    starttime = datetime.datetime.now()
    img = np.zeros([X,Y],dtype=np.uint8)
    img = BresenhamCircle_line_brush(img,400,400,200,10,255)
    endtime = datetime.datetime.now()
    print("Time:{}ms".format((endtime - starttime).microseconds))
    showImg(img,"Circle Line Brush (width=10)","outputs/Circle_Line_Brush1.jpg")

    starttime = datetime.datetime.now()
    img = np.zeros([X,Y],dtype=np.uint8)
    img = BresenhamCircle_line_brush(img,400,400,200,50,255)
    endtime = datetime.datetime.now()
    print("Time:{}ms".format((endtime - starttime).microseconds))
    showImg(img,"Circle Line Brush (width=50)","outputs/Circle_Line_Brush2.jpg")