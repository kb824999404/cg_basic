#同心圆圆弧生成算法
import cv2
import numpy as np
from utils import showImg
from circle import BresenhamCircle
import datetime

def circle_radius(img,x0,y0,r,width,color):
    for i in range(-width//2,width//2):
        img = BresenhamCircle(img,x0,y0,r+i,color)
    return img

if __name__=="__main__":
    X , Y = 800,800
 
    starttime = datetime.datetime.now()
    img = np.zeros([X,Y],dtype=np.uint8)
    img = circle_radius(img,400,400,200,10,255)
    endtime = datetime.datetime.now()
    print("Time:{}ms".format((endtime - starttime).microseconds))
    showImg(img,"Circle Radius (width=10)","outputs/Circle_Radius1.jpg")

    starttime = datetime.datetime.now()
    img = np.zeros([X,Y],dtype=np.uint8)
    img = circle_radius(img,400,400,200,50,255)
    endtime = datetime.datetime.now()
    print("Time:{}ms".format((endtime - starttime).microseconds))
    showImg(img,"Circle Radius (width=50)","outputs/Circle_Radius2.jpg")