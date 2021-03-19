echo off
set f=circle_gradual
g++ %f%.cpp ../include/tgaimage.cpp ../include/geometry.cpp -std=c++11 -o %f%.exe