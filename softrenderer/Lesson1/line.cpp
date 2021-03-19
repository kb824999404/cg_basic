#include "../include/tgaimage.h"
#include <cmath>
#include <iostream>

const TGAColor white = TGAColor(255,255,255,255);
const TGAColor red = TGAColor(255,0,0,255);

void drawPixel(int x,int y,const TGAColor& color,TGAImage& image){
    int width=image.get_width(),height=image.get_height();
    if(x>=0&&x<width&&y>=0&&y<height){
        image.set(x,y,color);
    }
}
// DDA画线法
void line_dda(int x0,int y0,int x1,int y1,
    const TGAColor& color,TGAImage& image)
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
    int x,y;
    float dx,dy,k;
    dx = x1-x0;
    dy = y1-y0;
    k = dy/dx;
    y = y0;
    for(x=x0;x<=x1;x++){
        if(step){
            drawPixel(int(y+0.5),x,color,image);
        }
        else{
            drawPixel(x,int(y+0.5),color,image);
        }
        y +=k;
    }

}
// 中点画线法
void line_middle(int x0,int y0,int x1,int y1,
    const TGAColor& color,TGAImage& image)
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
    int x,y,a,b,d,d1,d2;
    int dy=(y1>y0)?1:-1;
    a = y1-y0;
    b = x1-x0;
    d = 2*a+b;
    d1 = 2*a;
    d2 = 2*(a+b);
    x = x0, y = y0;
    while(x<x1){
        if(d<0){
            d+=d1;
            x++;
            y+=dy;
        }
        else
        {
            d+=d2;
            x++;
        }
        if(step){
            drawPixel(y,x,color,image);
        }
        else{
            drawPixel(x,y,color,image);
        }
    }

}
// Bresenham画线法
void line_bresenham(int x0,int y0,int x1,int y1,
    const TGAColor& color,TGAImage& image)
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

int main(int argc,char ** argv){
    TGAImage image(800,800,TGAImage::RGB);
    // line_bresenham(100,100,200,200,white,image);
    // line_dda(100,100,200,0,white,image);
    line_middle(100,100,200,0,white,image);
    image.flip_vertically();
    image.write_tga_file("line.tga");

    return 0;
}