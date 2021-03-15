#include "../include/tgaimage.h"

const TGAColor white = TGAColor(255,255,255,255);
const TGAColor red = TGAColor(255,0,0,255);




int main(int argc,char ** argv){
    TGAImage image(400,400,TGAImage::RGB);
    for(int i=0;i<200;i++){
        image.set(i,i,red);
    }
    image.flip_vertically();
    image.write_tga_file("first.tga");

    return 0;
}
