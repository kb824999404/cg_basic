#有线型的圆弧生成算法
import cv2
import numpy as np
from utils import drawPixel_symmetric,showImg

#Bresenham圆弧生成算法（有线型）
def BresenhamCircle_type(img,x0,y0,r,color,linetype=[1,1]):
    counter=0
    x=0;y=r
    d=3-2*r
    while x<=y:
        if  linetype[counter%len(linetype)]==1:
            img=drawPixel_symmetric(img,x0,y0,x,y,color)
        if d<0:
            d+=4*x+7
        else:
            d+=4*(x-y)+11
            y-=1
        x+=1
        counter+=1
    return img


if __name__=='__main__':
    X , Y = 100,100
    img = np.zeros([X,Y],dtype=np.uint8)
    img = BresenhamCircle_type(img,50,50,30,255,[1,0])
    showImg(img,"Circle Line Type1","outputs/Circle_Line_Type1.jpg")


    img = np.zeros([X,Y],dtype=np.uint8)
    img = BresenhamCircle_type(img,50,50,30,255,[1,1,0,0])
    showImg(img,"Circle Line Type2","outputs/Circle_Line_Type2.jpg")

    img = np.zeros([X,Y],dtype=np.uint8)
    img = BresenhamCircle_type(img,50,50,30,255,[1,0,1,1,1,0])
    showImg(img,"Circle Line Type3","outputs/Circle_Line_Type3.jpg")