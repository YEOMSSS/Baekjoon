#include <stdio.h>
#include <string.h>

int main(void)
{

    char string[1001];
    // gets(string);
    scanf("%s", string);

    char korea[] = {"KOREA"};

    int check = 0, result = 0;
    for (size_t i = 0; i < strlen(string); i++)
    {
        if (string[i] == korea[check])
        {
            result++;
            check = (check + 1) % 5;
        }
    }

    printf("%d", result);
    return 0;
}