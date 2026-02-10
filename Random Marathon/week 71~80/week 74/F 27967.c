#include <stdio.h>
#include <stdlib.h>

int check(int N, char arr[])
{
    int temp = 0;
    for (int i = 0; i < N; i++)
    {
        if (arr[i] == '(')
            temp++;
        else
            temp--;
    }
    // dfs에서 '('부터 확인하기 때문에 합이 0인지만 보면 된다.
    // 완전 무작위로 쌓았다면 위 과정에서 음수가 되는 순간이 있으면 안된다.
    if (!temp)
    {
        puts(arr);
        exit(0);
    }
    return 0;
}

void dfsR(int N, char arr[], int position)
{
    if (position == N)
    {
        if (!check(N, arr))
            return;
    }

    if (arr[position] == 'G')
    {
        arr[position] = '(';
        dfsR(N, arr, position + 1);
        arr[position] = ')';
        dfsR(N, arr, position + 1);
    }
    else
        dfsR(N, arr, position + 1);
}

int main(void)
{
    int N;
    scanf("%d", &N);

    char arr[N + 1];
    scanf("%s", arr);

    dfsR(N, arr, 0);

    return 0;
}