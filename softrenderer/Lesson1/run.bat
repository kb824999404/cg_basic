echo off
set f=sphere
g++ %f%.cpp ../include/tgaimage.cpp ../include/geometry.cpp -std=c++11 -o %f%.exe