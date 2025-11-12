#include <stdio.h>

int main(void)
{
    int arr[100][100] = {0};

    for (int i = 0; i < 4; i++)
    {
        int x1, y1, x2, y2;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

        for (int r = x1 - 1; r < x2 - 1; r++)
        {
            for (int c = y1 - 1; c < y2 - 1; c++)
                arr[r][c] = 1;
        }
    }

    int result = 0;
    for (int r = 0; r < 100; r++)
    {
        for (int c = 0; c < 100; c++)
        {
            if (arr[r][c])
                result++;
        }
    }

    printf("%d", result);
    return 0;
}