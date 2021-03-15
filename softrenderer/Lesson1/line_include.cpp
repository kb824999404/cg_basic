#include "../include/tgaimage.h"
#include "../include/color.h"
#include "../include/geometry.h"

int main(int argc,char ** argv){
    TGAImage image(800,800,TGAImage::RGB);
    Geometry::line(100,100,600,600,Color::white,image);
    image.flip_vertically();
    image.write_tga_file("line_include.tga");

    return 0;
}