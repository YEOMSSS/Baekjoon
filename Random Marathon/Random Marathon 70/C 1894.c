#include <stdio.h>

int main(void)
{

    while (1)
    {
        double x1, y1, x2, y2, x3, y3, x4, y4;
        if (scanf("%lf %lf %lf %lf %lf %lf %lf %lf", &x1, &y1, &x2, &y2, &x3, &y3, &x4, &y4) != 8)
            break;

        double ax, ay, dx, dy, bx, by, rx, ry;
        if (x1 == x3 && y1 == y3)
        { // 1 3
            dx = x1;
            dy = y1;
            ax = x2;
            ay = y2;
            bx = x4;
            by = y4;
        }
        else if (x1 == x4 && y1 == y4)
        { // 1 4
            dx = x1;
            dy = y1;
            ax = x2;
            ay = y2;
            bx = x3;
            by = y3;
        }
        else if (x2 == x3 && y2 == y3)
        { // 2 3
            dx = x2;
            dy = y2;
            ax = x1;
            ay = y1;
            bx = x4;
            by = y4;
        }
        else if (x2 == x4 && y2 == y4)
        { // 2 4
            dx = x2;
            dy = y2;
            ax = x1;
            ay = y1;
            bx = x3;
            by = y3;
        }

        rx = ax + bx - dx;
        ry = ay + by - dy;

        printf("%.3lf %.3lf\n", rx, ry);
    }
}
