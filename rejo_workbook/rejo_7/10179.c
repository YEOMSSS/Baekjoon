#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    while (N--)
    {
        double price;
        scanf("%lf", &price);

        printf("$%.2lf\n", price * 0.8);
    }
    return 0;
}