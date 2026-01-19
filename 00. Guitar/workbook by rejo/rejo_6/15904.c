#include <stdio.h>
#include <string.h>

int main(void)
{

    char string[1001];
    // gets(string);
    fgets(string, sizeof(string), stdin);

    char ucpc[] = {"UCPC"};

    int check = 0;
    for (size_t i = 0; i < strlen(string); i++)
    {
        if (string[i] == ucpc[check])
        {
            if (++check == 4)
            {
                printf("I love UCPC");
                return 0;
            }
        }
    }

    printf("I hate UCPC");
    return 0;
}