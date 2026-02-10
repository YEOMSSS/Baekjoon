// 상대는 중앙에 두려 할 것이고, 난 모서리에 둘 거야.
// 어느 모서리에 둬도 답이 없다면 그 칸을 막으면 된다.
// 어느 모서리에서라도 내가 둘 수 있으면 그 칸은 막을 필요가 없다.

#include <stdio.h>

int main(void)
{
    int N, M;
    scanf("%d %d", &N, &M);

    int D;
    scanf("%d", &D);

    int result = 0;
    //  좌상0,0 우상0,M-1 좌하N-1,0 우하N-1,M-1
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (i + j >= D) // 좌상
                continue;
            else if (i + M - 1 - j >= D) // 우상
                continue;
            else if (N - 1 - i + j >= D) // 좌하
                continue;
            else if (N - 1 - i + M - 1 - j >= D) // 우하
                continue;
            result++;
        }
    }

    printf("%d\n", result);
    return 0;
}
