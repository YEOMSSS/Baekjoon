/*
#include <stdio.h>
#include <string.h>

int main(void)
{
    char string[2502];
    fgets(string, sizeof(string), stdin);
    string[strcspn(string, "\n")] = '\0';

    char target[52];
    fgets(target, sizeof(target), stdin);
    target[strcspn(target, "\n")] = '\0';

    int count = 0;
    char *p = string; // p는 *p부터 시작하는 string 문자열이 된다.

    int len = strlen(target);
    while (1)
    {
        // p에 target이 있으면 target이 시작하는 포인터를 p에 반환, 못 찾으면 NULL
        // 그러니까 쉽게말하면, target의 위치를 반환한다는 거지.
        p = strstr(p, target);
        if (p == NULL)
            break;

        count++;
        // 겹치지 않게니까 target의 길이만큼 이동한다.
        p += len;
    }

    printf("%d\n", count);
    return 0;
}
*/

/*
#include <stdio.h>
#include <string.h>

int main(void)
{
    char string[2502];
    fgets(string, sizeof(string), stdin);
    string[strcspn(string, "\n")] = '\0';

    char target[52];
    fgets(target, sizeof(target), stdin);
    target[strcspn(target, "\n")] = '\0';

    int len_s = strlen(string);
    int len_t = strlen(target);

    if (len_t == 0)
    {
        printf("0\n");
        return 0;
    }

    int count = 0;
    int i = 0;

    while (i <= len_s - len_t)
    {
        int match = 1;
        for (int j = 0; j < len_t; j++)
        {
            if (string[i + j] != target[j])
            {
                match = 0;
                break;
            }
        }

        if (match)
        {
            count++;
            i += len_t;
        }
        else
        {
            i++;
        }
    }

    printf("%d\n", count);
    return 0;
}
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char string[2502];
    fgets(string, sizeof(string), stdin);
    string[strcspn(string, "\n")] = '\0';

    char target[52];
    fgets(target, sizeof(target), stdin);
    target[strcspn(target, "\n")] = '\0';

    if (strlen(target) == 0)
    {
        printf("0\n");
        return 0;
    }

    int cnt = 0, temp = 0, i = 0, j = 0;

    while (i < strlen(string))
    {
        if (string[i++] != target[j++])
        {
            j = 0;
            temp++;
            i = temp;
        }
        else if (j == strlen(target))
        {
            cnt++;
            j = 0;
            temp = i;
        }
    }
    printf("%d", cnt);
}
