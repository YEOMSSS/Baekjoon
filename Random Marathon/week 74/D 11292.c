#include <stdio.h>

struct student
{
    char name[11];
    float height;
};

int main(void)
{
    while (1)
    {
        int N;
        scanf("%d", &N);

        if (!N)
            return 0;

        struct student students[N];

        float tallest = 0;

        for (int i = 0; i < N; i++)
        {
            scanf("%s %f", students[i].name, &students[i].height);

            if (tallest < students[i].height)
                tallest = students[i].height;
        }

        for (int i = 0; i < N; i++)
        {
            if (students[i].height == tallest)
                printf("%s ", students[i].name);
        }
        putchar('\n');
    }
}