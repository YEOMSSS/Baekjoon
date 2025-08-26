#include <stdio.h>

int sum(int arr[], int len) {
    int total = 0;

    for (int i = 0; i < len; i++) {
        total += arr[i];
    }

    return total;
}

int main(void) {
    int T;
    scanf("%d", &T);

    for (int t = 0; t < T; t++) {
        int N;
        scanf("%d", &N);

        int arr[N];
        for (int i = 0; i < N; i++) {

            scanf("%d", &arr[i]);
        }

        printf("%d\n", sum(arr, N));
    }
    
    return 0;
}