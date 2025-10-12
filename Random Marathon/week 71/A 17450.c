#include <stdio.h>

long double func(int m, int w)
{
    int m10 = (m * 10 >= 5000) ? m * 10 - 500 : m * 10;
    return (long double)w * 10 / m10; // 변수형 처리에 주의할 것.
}

int main(void)
{
    int sm, sw, nm, nw, um, uw;
    scanf("%d %d %d %d %d %d", &sm, &sw, &nm, &nw, &um, &uw);
    long double s = func(sm, sw);
    long double n = func(nm, nw);
    long double u = func(um, uw);

    char result = 'S';
    long double temp = s;
    if (s < n)
    {
        temp = n;
        result = 'N';
    }
    if (temp < u)
    {
        temp = u;
        result = 'U';
    }
    putchar(result);

    return 0;
}