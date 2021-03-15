#include "../include/tgaimage.h"
#include <cmath>

const TGAColor white = TGAColor(255,255,255,255);
const TGAColor red = TGAColor(255,0,0,255);

void drawPixel(int x,int y,const TGAColor& color,TGAImage& image){
    int width=image.get_width(),height=image.get_height();
    if(x>=0&&x<width&&y>=0&&y<height){
        image.set(x,y,color);
    }
}

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
    line_bresenham(100,100,200,0,white,image);
    image.flip_vertically();
    image.write_tga_file("line.tga");

    return 0;
}