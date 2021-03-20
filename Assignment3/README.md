## 计算机图形学第三次作业——圆弧生成算法的改进

> 1851197 周楷彬

* 文件目录：
  * `circle/`：圆弧生成算法
    * `circle/circle.py`：基本圆弧生成算法
    * `circle_line_brush.py`：线刷子圆弧生成算法
    * `circle_square_brush.py`：方形刷子圆弧生成算法
    * `circle_radius.py`：同心圆圆弧生成算法
    * `circle_line_type.py`：有线型的圆弧生成算法
    * `circle/utils.py`：一些辅助函数
    * `circle/outputs/`：结果图片
  * `sphere/`：球面片生成算法
    * `sphere/include/three.js`：Three.JS代码
    * `sphere/sphere.html`：球面片生成算法可视化

## 1. 带宽度的圆弧生成算法

### 1.1 线刷子

#### 1.1.1 算法思想

* 与直线生成算法类似，按照原始的圆弧生成算法点亮栅格中的像素，与此同时在每次点亮的时候用一个具有一定宽度的“线刷子”点亮构成宽度的像素
* 按照**弧度**进行分类
  - 小于45度的圆弧（斜率小于1），采用水平线刷
  - 大于45度的圆弧（斜率大于1），采用垂直线刷

#### 1.1.2 算法实现

在Bresenham圆弧生成算法的基础上，实现有宽度的圆弧生成算法

```python
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
```

#### 1.1.3 算法结果

* **width=10：**
  
  * <center><img src="circle/outputs/Circle_Line_Brush1.jpg" style="zoom:50%;" /></center>
  * 执行时间：`6986ms`
* **width=50：**
  * <center><img src="circle/outputs/Circle_Line_Brush2.jpg" style="zoom:50%;" /></center>
  * 执行时间：`59874ms`

#### 1.1.4 算法评价

* **优点：**

  - 实现简单
* **缺点：**
  * 宽度较大时，生成的圆弧外侧带有缺口

---

### 1.2 方形刷子

#### 1.2.1 算法思想

* 与直线生成算法类似，将边宽为指定线宽的方形刷子的中心放在圆弧的起点，方形刷子的中心沿着圆弧移动，直到圆弧的终点

#### 1.2.2 算法实现

在Bresenham圆弧生成算法的基础上，实现有宽度的圆弧生成算法

```python
def BresenhamCircle_square_brush(img,x0,y0,r,width,color):
    x=0;y=r
    d=3-2*r
    while x<=y:
        for i in range(-width//2,width//2):
            for j in range(-width//2,width//2):
                #八个对称点
                img=drawPixel_symmetric(img,x0,y0,x+i,y+j,color)
        if d<0:
            d+=4*x+7
        else:
            d+=4*(x-y)+11
            y-=1
        x+=1
    return img
```

#### 1.2.3 算法结果

* **width=10：**
  * <center><img src="circle/outputs/Circle_Square_Brush1.jpg" style="zoom:50%;" /></center>
  * 执行时间：`71850ms`
* **width=50：**
  * <center><img src="circle/outputs/Circle_Square_Brush2.jpg" style="zoom:50%;" /></center>
  * 执行时间：`121890ms`

#### 1.2.4 算法评价

* **优点：**

  - 实现简单
  - 生成的圆弧不会出现缺口
* **缺点：**
  * 效率低：正方形的扫描方式导致相邻两个正方形有重叠
  * 正方形的扫描方式导致宽度较大时，圆弧宽度不均匀，圆的形状不规则

---

### 1.3 同心圆

#### 1.3.1 算法思想

* 在原始圆弧生成算法的基础上，以原始半径的圆弧为中心，根据宽度生成一组半径不一致的同心圆

#### 1.3.2 算法实现

```python
def circle_radius(img,x0,y0,r,width,color):
    for i in range(-width//2,width//2):
        img = BresenhamCircle(img,x0,y0,r+i,color)
    return img
```

#### 1.3.3 算法结果

* **width=10：**
  * <center><img src="circle/outputs/Circle_Radius1.jpg" style="zoom:50%;" /></center>
  * 执行时间：`9966ms`
* **width=50：**
  * <center><img src="circle/outputs/Circle_Radius2.jpg" style="zoom:50%;" /></center>
  * 执行时间：`76795ms`

#### 1.3.4 算法评价

* **优点：**
- 实现简单
  - 生成的圆弧不会出现缺口，且形状规则
* **缺点：**
  * 生成的圆弧带有孔洞

---

### 1.4 结果比较

| 宽度\算法 | 线刷子  | 方形算子 | 同心圆  |
| --------- | ------- | -------- | ------- |
| 10        | 6986ms  | 71850ms  | 9966ms  |
| 50        | 59874ms | 121890ms | 76795ms |



---

## 2. 有线型的圆弧生成算法

### 2.1 算法思想

* 用位串存放线型，线型进行周期性重复

### 2.2 算法实现

* `linetype`表示线型

```python
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
```

### 2.3 算法结果

* `1 0`：

  * <center><img src="circle/outputs/Circle_Line_Type1.jpg" style="zoom:67%;" /></center>

* `1 1 0 0`：

  * <center><img src="circle/outputs/Circle_Line_Type2.jpg" style="zoom:67%;" /></center>

* `1 0 1 1 1 0`：

  * <center><img src="circle/outputs/Circle_Line_Type3.jpg" style="zoom:67%;" /></center>

---

## 3. 球面片生成算法