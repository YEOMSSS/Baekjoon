#include <stdio.h>
#include <math.h>

int main(void)
{

    int N;
    scanf("%d", &N);

    double x1, y1, x2, y2;
    scanf("%lf %lf", &x1, &y1);
    N--;

    while (N--)
    {
        scanf("%lf %lf", &x2, &y2);
    }

    double result = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));

    printf("%.5lf", result);
    return 0;
}