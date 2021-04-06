# 有序边表算法
import cv2
import numpy as np
from numpy.core.numeric import Inf
from utils import drawPixel,showImg


class Edge:
    def __init__(self,x,dx,y_max):
        self.x = x
        self.dx = dx
        self.y_max = y_max
    def __str__(self) :
        return '({},{},{})'.format(self.x,self.dx,self.y_max)
    
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self) :
        return '({},{})'.format(self.x,self.y)

class Polygon:
    def __init__(self,points):
        self.points = points

    def draw(self,img,color):
        points = self.points
        n_points = len(points)
        y_min = self.getYmin()
        y_max = self.getYmax()
        n_lines = y_max - y_min + 2
        ET = [[] for i in range(n_lines)]
        AET = []

        #装配新边表
        for i in range(n_points):
            p1 = i
            if i < n_points-1:
                p2 = i+1
            else:   #最后一条边由最后一顶点和第一个顶点构成
                p2 = 0
            
            if points[p1].y > points[p2].y: 
                tmp = p1
                p1 = p2
                p2 = tmp
            
            # print(poins[p1],poins[p2],end='\t')
            
            if points[p2].y-points[p1].y  == 0:  #边斜率为0
                dx= points[p2].x-points[p1].x
            else:
                dx = (points[p2].x-points[p1].x)/(points[p2].y-points[p1].y)
            edge = Edge(points[p1].x,dx,points[p2].y)
            ET[points[p1].y-y_min+1].append(edge)
            # print(edge)

        print("Scan")
        #扫描线算法
        for i in range(n_lines):
            y_current = y_min + i
            #插入新边
            for e_new in ET[i]:
                index_insert = 0
                for e_old in AET:
                    if e_old.x > e_new.x:
                        break
                    index_insert+=1
                AET.insert(index_insert,e_new)
            
            #填充
            for j in range(len(AET)//2):
                x1 = int(AET[2*j].x)
                x2 = int(AET[2*j+1].x)
                for x in range(x1,x2):
                    img = drawPixel(img,x,y_current,color)

            #更新AET
            e_remove = []
            for j in range(len(AET)):
                if AET[j].y_max <= y_current:
                    e_remove.append(j)
                else:
                    AET[j].x += AET[j].dx
            AET = [ AET[j] for j in range(len(AET)) if not j in e_remove ]
            AET.sort(key=lambda e: e.x)
        return img
            
    #多边形顶点y坐标最小值
    def getYmin(self):
        y = Inf
        for p in self.points:
            if p.y < y:
                y = p.y
        return y
    #多边形顶点y坐标最大值
    def getYmax(self):
        y = -Inf
        for p in self.points:
            if p.y > y:
                y = p.y
        return y





if __name__=='__main__':
    X , Y = 200,200
    img = np.zeros([X,Y],dtype=np.uint8)
    poins = []
    poins.append(Point(20,20))
    poins.append(Point(50,10))
    poins.append(Point(110,30))
    poins.append(Point(110,80))
    poins.append(Point(50,50))
    poins.append(Point(20,70))
    polygon = Polygon(poins)
    img = polygon.draw(img,255)

    poins = []
    poins.append(Point(100,100))
    poins.append(Point(150,100))
    poins.append(Point(150,180))
    poins.append(Point(100,180))
    polygon = Polygon(poins)
    img = polygon.draw(img,200)

    showImg(img,"Edge Fill","pic/edge_fill.jpg")

