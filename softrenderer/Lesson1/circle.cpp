#include "../include/tgaimage.h"
#include <cmath>

const TGAColor white = TGAColor(255,255,255,255);
const TGAColor red = TGAColor(255,0,0,255);
const TGAColor green = TGAColor(0,255,0,255);
const TGAColor blue = TGAColor(0,0,255,255);

void drawPixel(int x,int y,const TGAColor& color,TGAImage& image){
    int width=image.get_width(),height=image.get_height();
    if(x>=0&&x<width&&y>=0&&y<height){
        image.set(x,y,color);
    }
}

void circle_middle(int x0,int y0,int r,const TGAColor& color,TGAImage& image){
    int x=0,y=r;
    int d=1.25-r;
    while (x<=y)
    {   
        // 八个对称点
        drawPixel(x0+x,y0+y,color,image);
        drawPixel(x0+y,y0+x,color,image);
        drawPixel(x0+y,y0-x,color,image);
        drawPixel(x0+x,y0-y,color,image);
        drawPixel(x0-x,y0+y,color,image);
        drawPixel(x0-y,y0+x,color,image);
        drawPixel(x0-y,y0-x,color,image);
        drawPixel(x0-x,y0-y,color,image);
        if(d<0){
            d+= 2*x+3;
            x++;
        }
        else{
            d+= 2*(x-y)+5;
            x++;
            y--;
        }
    }
    
}

void circle_bresenham(int x0,int y0,int r,const TGAColor& color,TGAImage& image){
    int x=0,y=r;
    int d=3-2*r;
    while (x<=y)
    {
        // 八个对称点
        drawPixel(x0+x,y0+y,color,image);
        drawPixel(x0+y,y0+x,color,image);
        drawPixel(x0+y,y0-x,color,image);
        drawPixel(x0+x,y0-y,color,image);
        drawPixel(x0-x,y0+y,color,image);
        drawPixel(x0-y,y0+x,color,image);
        drawPixel(x0-y,y0-x,color,image);
        drawPixel(x0-x,y0-y,color,image);
        if(d<0){
            d+=4*x+7;
        }
        else{
            d+=4*(x-y)+11;
            y--;
        }
        x++;
    }
    
}

void circle_positive_negative(int x0,int y0,int r,const TGAColor& color,TGAImage& image){
    int x=0,y=r;
    int f=0;
    while (x<=y)
    {
        // 八个对称点
        drawPixel(x0+x,y0+y,color,image);
        drawPixel(x0+y,y0+x,color,image);
        drawPixel(x0+y,y0-x,color,image);
        drawPixel(x0+x,y0-y,color,image);
        drawPixel(x0-x,y0+y,color,image);
        drawPixel(x0-y,y0+x,color,image);
        drawPixel(x0-y,y0-x,color,image);
        drawPixel(x0-x,y0-y,color,image);
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


int main(int argc,char ** argv){
    TGAImage image(800,800,TGAImage::RGB);
    circle_middle(400,400,100,red,image);
    circle_bresenham(400,400,200,green,image);
    circle_positive_negative(400,400,300,blue,image);
    image.flip_vertically();
    image.write_tga_file("circle.tga");

    return 0;
}