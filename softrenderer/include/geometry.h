#ifndef __GEOMETRY_H__
#define __GEOMETRY_H__
#include "tgaimage.h"

namespace Geometry{
    void drawPixel(int x,int y,const TGAColor& color,TGAImage& image);
    void line(int x0,int y0,int x1,int y1,const TGAColor& color,TGAImage& image);
}

#endif