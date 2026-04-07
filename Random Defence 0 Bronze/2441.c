#include <stdio.h>

int main(void) {

    int N;
    scanf("%d", &N);

    for (int i = N; i > 0; i--) {
        for (int k = 0; k < N - i; k++) {
            putchar(' ');
        }
        for (int j = i; j > 0; j--) {
            putchar('*');
        }
        putchar('\n');
    }
    return 0;
}