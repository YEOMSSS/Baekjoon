
#include <stdio.h>

int main(void)
{
    char string[101];

    while (fgets(string, 101, stdin) != NULL)
    {
        printf("%s", string);
    }
    return 0;
}

/*
// scanf 방식은 빈 줄을 처리하지 못한다.
#include <stdio.h>

int main(void)
{
    char string[101];
    while (scanf("%100[^\n]", string) == 1) // %[^\n]은 줄 끝 개행 전까지 읽기
    {
        printf("%s\n", string);
        getchar(); // 개행 문자 소비. 개행 전까지만 읽었기 때문에 빼내줘야 한다.
    }
    return 0;
}
*/