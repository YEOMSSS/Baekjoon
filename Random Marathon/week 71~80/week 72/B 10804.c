
#include <stdio.h>

int main(void)
{
    int arr[20];
    for (int i = 0; i < 20; i++)
    {
        arr[i] = i + 1;
    }

    int N = 10;
    while (N--)
    {
        int ai, bi;
        scanf("%d %d", &ai, &bi);

        while (ai < bi)
        {
            int temp;
            temp = arr[ai - 1];
            arr[ai - 1] = arr[bi - 1];
            arr[bi - 1] = temp;

            ai++;
            bi--;
        }
    }
    for (int i = 0; i < 20; i++)
    {
        printf("%d ", arr[i]);
    }
    return 0;
}