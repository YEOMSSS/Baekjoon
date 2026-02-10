
// 범위를 생각해봐. 수직선을 긋고 점을 찍어봐.
// 겹치는 부분만 선택하면 되는 거야.

#include <stdio.h>

int main(void) {
    int A, B, K, X;
    scanf("%d %d %d %d", &A, &B, &K, &X);

    if ((K + X) < A || B < (K - X)) {
        printf("IMPOSSIBLE");

        return 0;
    }

    int start, end;

    if ((K - X) < A) {
        start = A;
    } else if (A < (K - X)) {
        start = (K - X);
    }

    if ((K + X) < B) {
        end = K + X;
    } else if (B < (K + X)) {
        end = B;
    }

    printf("%d", (end - start + 1));

    return 0;

}
