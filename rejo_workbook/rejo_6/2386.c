
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    while (1)
    {
        char string[254];
        fgets(string, sizeof(string), stdin);

        if (string[0] == '#')
            return 0;

        int count = 0;
        int len = strlen(string);
        char check = string[0];

        for (int i = 2; i < len; i++)
            if (tolower(string[i]) == check)
                count++;

        printf("%c %d\n", check, count);
    }

    return 0;
}