#include <stdio.h>
#include <string.h>

int main(void)
{
    while (1)
    {
        char string[81];
        fgets(string, sizeof(string), stdin);
        // fgets로 받았으면 개행 제거 잘해주자.
        string[strcspn(string, "\n")] = '\0';

        if (!strcmp(string, "***"))
            return 0;

        int len = strlen(string);
        for (int i = len - 1; i >= 0; i--)
        {
            putchar(string[i]);
        }
        putchar('\n');
    }

    return 0;
}