
// aeiou를 만나면 두칸 건너뛰어 읽기

#include <stdio.h>

int main(void)
{

    char arr[101];
    gets(arr); // 써도되는겨? 되긴하네.

    for (int i = 0; arr[i]; i++)
    {
        printf("%c", arr[i]);
        if (arr[i] == 'a' || arr[i] == 'e' || arr[i] == 'i' || arr[i] == 'o' || arr[i] == 'u')
            i += 2;
    }
    return 0;
}