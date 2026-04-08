
// 뒤에서부터, 큰 수에서부터 정렬하는 선택정렬을 해 보자.
// 이번엔 K번 교환 후 stop한다.
// 근데 이제 500000크기의 배열이 들어온다면? 시간초과가 나겠지. O(N2)니까.
// 그럼 어떻게 해야하지?

// 선택정렬은 자신 제외를 계속해서 순회하며 비교해야해서 오래걸린다.
// 그래서 오름차순된 배열을 따로 하나 만들 거다. 선택정렬 없이 빠르게.
// 그리고 그거랑 비교해서 바로 바꿔버릴거다. 선택정렬인 척 답만 내도록.

#include <stdio.h>
#include <stdlib.h> //malloc, qsort, bsearch

// qsort용 함수
int compare(const void *a, const void *b)
{
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y); // 오름차순
}

int main(void)
{
    int N, K;
    scanf("%d %d", &N, &K);

    int *A = malloc(N * sizeof(int));
    int *B = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++)
    { // 비교용으로 B배열도 만들어준다.
        scanf("%d", &A[i]);
        B[i] = A[i];
    }

    // 인덱스 찾는 용으로 B배열을 오름차순 정렬해준다.
    qsort(B, N, sizeof(int), compare);

    int *pos = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++)
    {
        // bsearch는 B 배열 안에서 A[i] 값을 찾아서, 그 주소를 반환한다.
        int *p = bsearch(&A[i], B, N, sizeof(int), compare);
        // 현주소 - 첫주소 = 현 인덱스(원소 간 거리)
        int rank = (int)(p - B);
        // pos[rank] = i는 B[rank]가 현재 A[i]에 있다를 의미함.
        pos[rank] = i;
    }

    int cnt = 0;
    for (int i = N - 1; i >= 0; i--)
    {
        int need = B[i];      // i에 있어야 하는 값
        int current = pos[i]; // i에 있어야 하는 값의 현재 인덱스

        // 현 인덱스에 있어야 하는 값이 없는 경우
        if (current != i)
        {
            int x = A[i]; // 현재 값(i에 있던 값)
            int *px = bsearch(&x, B, N, sizeof(int), compare);
            int x_rank = (int)(px - B); // 현재 값이 있어야 하는 인덱스

            // 원소 갱신
            A[current] = x;
            A[i] = need;

            // 위치 갱신. A[i]는 정렬되었고, A[current]가 원래 있던 값으로 바뀐다.
            pos[i] = i;            // 전부 pos[i] = i가 되면 정렬된 것이다.
            pos[x_rank] = current; // B[x_rank]가 현재 A[current]에 있다.

            cnt++;
            if (cnt == K)
            { // K번째 교환 후 배열을 출력
                for (int i = 0; i < N; i++)
                { // 처음만 빼고 공백 출력
                    if (i != 0)
                        putchar(' ');
                    printf("%d", A[i]);
                }

                free(A);
                free(B);
                free(pos);

                return 0;
            }
        }
    }

    printf("-1");

    free(A);
    free(B);
    free(pos);

    return 0;
}

// 씨발
