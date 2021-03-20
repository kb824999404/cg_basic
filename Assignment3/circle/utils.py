import matplotlib.pyplot as plt
import cv2

#绘制像素,带边界检测
def drawPixel(img,x,y,color):
    Y,X = img.shape[0],img.shape[1]
    if x>=0 and x<X  and y>=0 and y<Y:
        img[y,x] = color
    return img
#绘制八个对称的像素点
def drawPixel_symmetric(img,x0,y0,x,y,color):
    img=drawPixel(img,x0+x,y0+y,color)
    img=drawPixel(img,x0+y,y0+x,color)
    img=drawPixel(img,x0+y,y0-x,color)
    img=drawPixel(img,x0+x,y0-y,color)
    img=drawPixel(img,x0-x,y0+y,color)
    img=drawPixel(img,x0-y,y0+x,color)
    img=drawPixel(img,x0-y,y0-x,color)
    img=drawPixel(img,x0-x,y0-y,color)
    return img
#显示图片,保存图片
def showImg(img,title="Image",path=None):
    X,Y = img.shape[0],img.shape[1]
    axis = plt.gca()
    axis.set_ylim((0, Y))
    axis.set_xlim((0, X))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(title)
    plt.imshow(img,cmap="gray",vmin=0, vmax=255)
    if path:
        plt.savefig(path)
    plt.show()