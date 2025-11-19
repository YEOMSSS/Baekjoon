#include <stdio.h>
#include <string.h>

int main(void)
{
    char string[101];
    scanf("%s", string);

    int len = strlen(string);

    int row;
    for (int i = 1; i * i <= len + 1; i++)
    {
        if (len % i)
            continue;
        row = i;
    }
    int col = len / row;

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            // printf("%c", string[j * row + i]);
            putchar(string[j * row + i]);
        }
    }
    return 0;
}