
#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int a;
    scanf("%d", &a);
    N--;

    long result = 0, acc = a;

    while (N--)
    {
        int num;
        scanf("%d", &num);

        result += acc * num;
        acc += num;
    }

    printf("%ld", result);
    return 0;
}