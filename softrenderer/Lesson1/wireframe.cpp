#include "../include/tgaimage.h"
#include "../include/color.h"
#include "../include/geometry.h"
#include "../include/model.h"

int main(int argc,char ** argv){
    TGAImage image(800,800,TGAImage::RGB);

    // Model *model = new Model("model.obj");


    // Geometry::line(100,100,600,600,Color::white,image);
    // image.flip_vertically();
    // image.write_tga_file("wireframe.tga");

    return 0;
}