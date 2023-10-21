#include <graphics.h>
#include <conio.h>
#include<stdio.h>
int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    int x = 200, y = 200, radius = 100;
    circle(x, y, radius);
    getch();
    closegraph();
    return 0;
}
