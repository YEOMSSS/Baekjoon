#include <stdio.h>
#include <string.h>

int main(void)
{
    int T;
    scanf("%d", &T);

    while (T--)
    {
        int idx;
        scanf("%d", &idx);
        idx--;

        char string[81];
        scanf("%s", string);

        int len = strlen(string);

        for (int i = 0; i < len; i++)
        {
            if (i == idx)
                continue;

            putchar(string[i]);
        }
        putchar('\n');
    }
    return 0;
}