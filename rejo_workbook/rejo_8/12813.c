#include <stdio.h>

const int NUM = 100000;

int main(void)
{
    char A[NUM + 1];
    char B[NUM + 1];

    scanf("%s", A);
    scanf("%s", B);

    char ans_and[NUM + 1];
    char ans_or[NUM + 1];
    char ans_xor[NUM + 1];
    char ans_notA[NUM + 1];
    char ans_notB[NUM + 1];

    for (int i = 0; i < NUM; i++)
    {
        char a = A[i];
        char b = B[i];

        if (a == '1' && b == '1')
            ans_and[i] = '1';
        else
            ans_and[i] = '0';

        if (a == '1' || b == '1')
            ans_or[i] = '1';
        else
            ans_or[i] = '0';

        if (a != b)
            ans_xor[i] = '1';
        else
            ans_xor[i] = '0';

        if (a == '0')
            ans_notA[i] = '1';
        else
            ans_notA[i] = '0';

        if (b == '0')
            ans_notB[i] = '1';
        else
            ans_notB[i] = '0';
    }

    ans_and[NUM] = '\0';
    ans_or[NUM] = '\0';
    ans_xor[NUM] = '\0';
    ans_notA[NUM] = '\0';
    ans_notB[NUM] = '\0';

    printf("%s\n", ans_and);
    printf("%s\n", ans_or);
    printf("%s\n", ans_xor);
    printf("%s\n", ans_notA);
    printf("%s\n", ans_notB);

    return 0;
}