#include <stdio.h>

int main(void) {

    int AB, BC, CD;
    scanf("%d %d %d", &AB, &BC, &CD);

    double result = (double)AB * CD / BC;
    printf("%.6f", result);

    return 0;
}

// 10의 -6승 오차범위니까 %.6f면 충분하다.