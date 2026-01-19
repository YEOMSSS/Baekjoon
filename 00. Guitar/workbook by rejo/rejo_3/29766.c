#include <stdio.h>
#include <string.h>

int main(void)
{
    char string[1001];
    scanf("%s", string);

    int len = strlen(string), result = 0;

    for (int i = 0; i + 3 < len; i++)
        if (string[i] == 'D' && string[i + 1] == 'K' && string[i + 2] == 'S' && string[i + 3] == 'H')
            result++;

    // for (size_t i = 0; i < strlen(string); i++)
    // {

    //     if (string[i] == 'D')
    //         check = 1;
    //     else if (string[i] == 'K' && check == 1)
    //         check++;
    //     else if (string[i] == 'S' && check == 2)
    //         check++;
    //     else if (string[i] == 'H' && check == 3)
    //     {
    //         result++;
    //         check = 0;
    //     }
    //     else
    //         check = 0;

    printf("%d", result);
    return 0;
}
