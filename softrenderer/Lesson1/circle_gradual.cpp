#include "../include/tgaimage.h"
#include "../include/geometry.h"
#include <cstdlib>
#include <ctime>
using namespace Geometry;


int main(int argc,char ** argv){
    TGAImage image(800,800,TGAImage::RGB);
    srand(time(NULL));
    for(int i=0;i<400;i++){
        int v = 256*i/400;
        TGAColor color= TGAColor(0,v,v,255);
        circle(400,400,i,color,image);
    }
    image.flip_vertically();
    image.write_tga_file("circle_gradual.tga");

    return 0;
}