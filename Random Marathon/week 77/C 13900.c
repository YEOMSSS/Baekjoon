/*
ab  ac  ad  a(b+c+d)
    bc  bd  b(c+d)
        cd  c(d)
이게낫겠다.
da  db  dc  d(a+b+c)
ca  cb      c(a+b)
ba          b(a)
*/

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