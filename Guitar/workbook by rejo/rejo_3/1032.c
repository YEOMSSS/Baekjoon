#include <stdio.h>
#include <string.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    char string[51];
    scanf("%s", string);
    int len = strlen(string);
    N--;

    while (N--)
    {
        char string2[len + 1];
        scanf("%s", string2);
        for (int i = 0; i < len; i++)
        {
            if (string[i] != string2[i])
            {
                string[i] = '?';
            }
        }
    }

    printf("%s", string);

    return 0;
}