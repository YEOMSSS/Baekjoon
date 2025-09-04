
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char input[3]; // 두자리까지만 받을거니까 3으로
    fgets(input, 3, stdin);
    input[strcspn(input, "\n")] = '\0'; // 공백 제거를 잘 해주자.

    if (strlen(input) == 1)
    {
        input[1] = input[0];
        input[0] = '0';
        input[2] = '\0';
    }

    char original[3];
    strcpy(original, input);
    int cnt = 0;

    do
    {
        int a = input[0] - '0';
        int b = input[1] - '0';
        int sum = (a + b) % 10;

        char next[3];
        next[0] = input[1];
        next[1] = (char)('0' + sum);
        next[2] = '\0';

        strcpy(input, next);
        cnt++;
    } while (strcmp(original, input) != 0);

    printf("%d", cnt);

    return 0;
}

/*
#include <stdio.h>

int main(void)
{
    int n; scanf("%d", &n);
    n %= 100;
    int orig = n, cnt = 0;

    do {
        int a = n / 10, b = n % 10;
        n = b * 10 + (a + b) % 10;
        cnt++;
    } while (n != orig);

    printf("%d\n", cnt);
    return 0;
}

*/