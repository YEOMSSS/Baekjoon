// 조금 생각을 해볼까?
// 결국 글자 하나를 꺼내서 맨 뒤로 옮기는 방식을 쓰면 되잖아?
// 모든 알파벳의 개수를 세서 결과가 각각 더 적으면 되는것.

#include <stdio.h>

int main(void)
{
    int alpha[26] = {0};

    char old[10001];
    scanf("%s", old);
    // 앞으로 굳이 len구하지 말고 이런식으로 해야겠다.
    // \0이 되면 알아서 멈춘다.
    for (int i = 0; old[i]; i++)
    {
        alpha[old[i] - 'A']++;
    }

    char new[10001];
    scanf("%s", new);
    for (int i = 0; new[i]; i++)
    {
        alpha[new[i] - 'A']--;
    }

    for (int i = 0; i < 26; i++)
    {
        if (alpha[i] < 0)
        {
            printf("NEED FIX");
            return 0;
        }
    }
    printf("OK");
    return 0;
}