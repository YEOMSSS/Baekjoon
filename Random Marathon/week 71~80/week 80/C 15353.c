#include <stdio.h>
#include <string.h>

#define MAXLEN 10010

char arr[3][MAXLEN + 1];

// 배열을 받을 것이므로 첫 주소를 가져와야 한다. 매개변수는 항상 포인터로 선언할 것.
// void add_str(const char *a, const char *b, char *out)
void add_str(const char a[], const char b[], char out[])
{
    // 널문자 제거를 위해 int형으로 변환 후 -1을 한다.
    int i = (int)strlen(a) - 1;
    int j = (int)strlen(b) - 1;
    int k = 0;
    int carry = 0;

    char tmp[MAXLEN + 1];

    // 맨 뒷자리부터 int로 변환해 더하기
    // a나 b가 남았거나, 올림이 존재하는 경우 반복
    while (i >= 0 || j >= 0 || carry)
    {
        // i나 j가 음수가 되면 그 숫자는 더 읽을게 없으니 그 자릿수는 0이다.
        int da = (i >= 0) ? a[i--] - '0' : 0;
        int db = (j >= 0) ? b[j--] - '0' : 0;

        int s = da + db + carry;
        // tmp에는 실제 숫자와는 역순으로 저장된다.
        tmp[k++] = (char)('0' + (s % 10));
        carry = s / 10;
    }
    // tmp를 다시 뒤집어서 정상 숫자로 만든다.
    for (int t = 0; t < k; ++t)
        out[t] = tmp[k - 1 - t];

    out[k] = '\0';
}

int main(void)
{
    scanf("%s %s", arr[0], arr[1]);

    add_str(arr[0], arr[1], arr[2]);

    puts(arr[2]);
    return 0;
}
