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

void drawPixel_symmetric(int x0,int y0,int x,int y,const TGAColor& color,TGAImage& image){
    drawPixel(x0+x,y0+y,color,image);
    drawPixel(x0+y,y0+x,color,image);
    drawPixel(x0+y,y0-x,color,image);
    drawPixel(x0+x,y0-y,color,image);
    drawPixel(x0-x,y0+y,color,image);
    drawPixel(x0-y,y0+x,color,image);
    drawPixel(x0-y,y0-x,color,image);
    drawPixel(x0-x,y0-y,color,image);
}


void circle_bresenham(int x0,int y0,int r,const TGAColor& color,TGAImage& image,int z){
    int x=0,y=r;
    int d=3-2*r;
    while (x<=y)
    {
        // 八个对称点
        drawPixel_symmetric(x0,y0,x,y,color,image);
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

void sphere_bresenham(int x0,int y0,int z0,int r,const TGAColor& color,TGAImage& image){
    int c=0; //截面半径
    int z=r; //z坐标
    int d=3-2*r;
    while(c<=z)
    {
        float v=float(c)/r;
        circle_bresenham(x0,y0,c,color*v,image,z);
        circle_bresenham(x0,y0,z,color*v,image,c);
        circle_bresenham(x0,y0,c,color*v,image,-z);
        circle_bresenham(x0,y0,z,color*v,image,-c);
        circle_bresenham(x0,y0,-c,color*v,image,z);
        circle_bresenham(x0,y0,-z,color*v,image,c);
        circle_bresenham(x0,y0,-c,color*v,image,-z);
        circle_bresenham(x0,y0,-z,color*v,image,-c);
        if(d<0)
        {
            d+=4*c+7;
        }
        else
        {
            d+=4*(c-z)+11;
            z--;
        }
        c++;
    }
}

int main(int argc,char ** argv){
    TGAImage image(800,800,TGAImage::RGB);
    sphere_bresenham(400,400,0,200,green,image);
    image.flip_vertically();
    image.write_tga_file("sphere.tga");

    return 0;
}