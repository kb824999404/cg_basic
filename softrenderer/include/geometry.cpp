#include "geometry.h"
#include <cmath>

void Geometry::drawPixel(int x,int y,const TGAColor& color,TGAImage& image){
    int width=image.get_width(),height=image.get_height();
    if(x>=0&&x<width&&y>=0&&y<height){
        image.set(x,y,color);
    }
}  

void Geometry::line(int x0,int y0,int x1,int y1,const TGAColor& color,TGAImage& image)
{
    bool step=false;
    if(abs(y1-y0)>abs(x1-x0)){        //k不属于[-1,1]
        std::swap(x0,y0);
        std::swap(x1,y1);
        step = true;
    }
    if (x0>x1) {    // make it left−to−right 
        std::swap(x0, x1); 
        std::swap(y0, y1); 
    } 
    int dx = x1-x0;
    int dy = y1-y0;
    int derror2 = std::abs(dy)*2; 
    int error2 = 0; 
    int e=-dx,y=y0;
    for(int x=x0;x<=x1;x++){
        if(step){
            drawPixel(y,x,color,image);
        }
        else{
            drawPixel(x,y,color,image);
        }
        error2 += derror2;
        if(error2 > dx){
            y += (y1>y0?1:-1); 
            error2 -= dx*2;
        }
    }
}

void Geometry::drawPixel_symmetric(int x0,int y0,int x,int y,const TGAColor& color,
    TGAImage& image)
{
    Geometry::drawPixel(x0+x,y0+y,color,image);
    Geometry::drawPixel(x0+y,y0+x,color,image);
    Geometry::drawPixel(x0+y,y0-x,color,image);
    Geometry::drawPixel(x0+x,y0-y,color,image);
    Geometry::drawPixel(x0-x,y0+y,color,image);
    Geometry::drawPixel(x0-y,y0+x,color,image);
    Geometry::drawPixel(x0-y,y0-x,color,image);
    Geometry::drawPixel(x0-x,y0-y,color,image);
}

void Geometry::circle(int x0,int y0,int r,const TGAColor& color,TGAImage& image){
    int x=0,y=r;
    int f=0;
    while (x<=y)
    {
        // 八个对称点
        drawPixel_symmetric(x0,y0,x,y,color,image);
        if(f<0){
            f+=2*x+1;
            x++;
        }
        else{
            f+=1-2*y;
            y--;
        }
    }
    
}