
#include <stdio.h>

int main() {
    
    int sum = 0;

    for (int i = 0; i < 5; i++) {
        int X;
        scanf("%d", &X);
        sum += X;
    }

    printf("%d", sum);

    return 0;
}

// sum(map(int, input().split()))
// 한줄이면 될 걸... 뭐 이리 복잡하냐.
