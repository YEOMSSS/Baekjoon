#include <stdio.h>
#include <stdlib.h>

int func(char board[3][4], int ax, int ay, int bx, int by, int cx, int cy, char mark)
{
    int empty = 0, cnt = 0;
    board[ax][ay] == mark ? cnt++ : empty++;
    board[bx][by] == mark ? cnt++ : empty++;
    board[cx][cy] == mark ? cnt++ : empty++;

    if (empty == 1 && cnt == 2)
    {
        board[ax][ay] = mark;
        board[bx][by] = mark;
        board[cx][cy] = mark;

        for (int i = 0; i < 3; i++)
            printf("%s\n", board[i]);

        return 1;
    }
    return 0;
}

int main(void)
{
    int N;
    scanf("%d", &N);

    for (int n = 1; n <= N; n++)
    {
        char board[3][4];
        for (int i = 0; i < 3; i++)
            scanf("%s", board[i]);

        getchar();
        char mark = getchar();

        printf("Case %d:\n", n);

        if (func(board, 0, 0, 0, 1, 0, 2, mark))
            continue;
        if (func(board, 1, 0, 1, 1, 1, 2, mark))
            continue;
        if (func(board, 2, 0, 2, 1, 2, 2, mark))
            continue;
        if (func(board, 0, 0, 1, 0, 2, 0, mark))
            continue;
        if (func(board, 0, 1, 1, 1, 2, 1, mark))
            continue;
        if (func(board, 0, 2, 1, 2, 2, 2, mark))
            continue;
        if (func(board, 0, 0, 1, 1, 2, 2, mark))
            continue;
        if (func(board, 0, 2, 1, 1, 2, 0, mark))
            continue;
    }
    return 0;
}