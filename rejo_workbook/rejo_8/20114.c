#include <stdio.h>

int main(void)
{
    int N, H, W;
    scanf("%d %d %d", &N, &H, &W);

    char string[N * W];

    char result[N + 1];
    for (int i = 0; i < N; i++)
        result[i] = '?';
    result[N] = '\0';

    for (int i = 0; i < H; i++)
    {
        scanf("%s", string);

        char cur_arr;
        for (int j = 0; j < N; j++)
        {
            // 이미 찾은 글자면 바로 continue
            if (result[j] != '?')
                continue;

            cur_arr = '?';
            for (int k = 0; k < W; k++)
            {
                cur_arr = string[j * W + k];
                if (cur_arr != '?')
                    break;
            }

            result[j] = cur_arr;
        }
    }

    printf("%s", result);
}