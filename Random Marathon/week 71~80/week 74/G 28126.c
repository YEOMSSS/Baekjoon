// 사용가능한 명령의 순서는 의미가 없어보인다. 어차피 더하기인데.
// 우선 대각선으로 갈수있을만큼 간 후 up이나 right를 쓰면 될 듯.

#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    char command[N + 1]; // \0이 들어갈 공간을 잊지 말아다오. 크아아악
    scanf("%s", command);

    int cnt_R = 0, cnt_U = 0, cnt_X = 0;

    for (int i = 0; i < N; i++)
    {
        char temp = command[i];

        switch (temp)
        {
        case 'R':
            cnt_R++;
            break;
        case 'U':
            cnt_U++;
            break;
        case 'X':
            cnt_X++;
            break;
        }
    }

    int K;
    scanf("%d", &K);

    int result = 0;
    while (K--)
    {
        int x, y;
        scanf("%d %d", &x, &y);

        x--;
        y--;
        int temp = x < y ? x : y;
        temp = temp < cnt_X ? temp : cnt_X;

        x -= temp;
        y -= temp;

        if (x <= cnt_R && y <= cnt_U)
        {
            result++;
        }
    }

    printf("%d", result);
    return 0;
}