import matplotlib.pyplot as plt

#绘制像素,带边界检测
def drawPixel(img,x,y,color):
    Y,X = img.shape[0],img.shape[1]
    if x>=0 and x<X  and y>=0 and y<Y:
        img[y,x] = color
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
    plt.imshow(img,vmin=0, vmax=255)
    if path:
        plt.savefig(path)
    plt.show()