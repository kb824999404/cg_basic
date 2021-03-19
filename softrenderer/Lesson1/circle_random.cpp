#include "../include/tgaimage.h"
#include "../include/geometry.h"
#include <cstdlib>
#include <ctime>
using namespace Geometry;


int main(int argc,char ** argv){
    TGAImage image(800,800,TGAImage::RGB);
    srand(time(NULL));
    for(int i=0;i<200;i++){
        int r = rand()%256;
        int g = rand()%256;
        int b = rand()%256;
        TGAColor color= TGAColor(r,g,b,255);
        circle(400,400,i*2,color,image);
        circle(400,400,i*2+1,color,image);
    }
    image.flip_vertically();
    image.write_tga_file("circle_random.tga");

    return 0;
}