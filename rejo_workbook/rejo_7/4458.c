#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);
    getchar();

    while (N--)
    {
        char string[32];

        fgets(string, sizeof(string), stdin);
        if (string[0] >= 97)
            string[0] = string[0] - 32;

        printf("%s", string);
    }
    return 0;
}