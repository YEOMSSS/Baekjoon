#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    char *ptr_arr_check[N];
    for (int i = 0; i < N; i++)
    {
        ptr_arr_check[i] = malloc(21);
        scanf("%20s", ptr_arr_check[i]);
    }

    char *ptr_arr[N - 1];
    for (int i = 0; i < N - 1; i++)
    {
        // malloc은 기본적으로 반환형이 void*이기 때문에 형변환cast해서 쓰기 편하다.
        // 이 경우는 char 하나를 저장할 수 있는 공간을 할당받고, 그 주소를 ptr_arr[i]가 가리키도록 한다.
        // c언어의 경우는 malloc을 형변환할 필요는 없다. 그리고 sizeof(char)는 1이다.
        ptr_arr[i] = malloc(21);
        // ptr_arr[i] = (char *)malloc(100 * sizeof(char));
        scanf("%20s", ptr_arr[i]);
    }

    for (int i = 0; i < N; i++)
    {
        char *ingredients = ptr_arr_check[i];

        int check = 0;
        for (int j = 0; j < N - 1; j++)
        {
            // strcmp는 같으면 0, 다르면 0이 아닌 수를 반환(+ or -)
            if (strcmp(ptr_arr[j], ingredients) == 0)
            {
                check = 1;
                break;
            }
        }
        if (!check)
        {
            puts(ingredients);
            for (int k = 0; k < N; k++)
                free(ptr_arr_check[k]);
            for (int k = 0; k < N - 1; k++)
                free(ptr_arr[k]);
            return 0;
        }
    }

    for (int k = 0; k < N; k++)
        free(ptr_arr_check[k]);
    for (int k = 0; k < N - 1; k++)
        free(ptr_arr[k]);
    return 0;
}
