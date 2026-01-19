#include <stdio.h>

int main(void)
{
    int answer = 0;
    int current = 0;

    for (int i = 0; i < 4; i++)
    {
        int off, on;
        scanf("%d %d", &off, &on);

        current = current - off + on;
        if (answer < current)
            answer = current;
    }

    printf("%d", answer);

    return 0;
}