#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>

int main(void)
{
    int T;
    scanf("%d", &T);

    while (T--)
    {
        int c;
        scanf("%d", &c);

        double a, b;
        scanf("%lf %lf", &a, &b);

        if (c == 1)
        {
            double r = sqrt(pow(a, 2) + pow(b, 2));
            double t = atan2(b, a);
            if (t < 0)
            {
                t += M_PI * 2;
            }
            printf("%.6lf %.6lf\n", r, t);
        }

        if (c == 2)
        {
            double x = a * cos(b);
            double y = a * sin(b);

            printf("%.6lf %.6lf\n", x, y);
        }
    }

    return 0;
}
