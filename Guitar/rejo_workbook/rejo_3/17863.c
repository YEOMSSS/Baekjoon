#include <stdio.h>

int main(void)
{
    char arr[8];
    scanf("%s", arr);

    for (int i = 0; i < 3; i++)
    {
        if (arr[i] != '5')
        {
            printf("NO");
            return 0;
        }
    }
    printf("YES");
    return 0;
}