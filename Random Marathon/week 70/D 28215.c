#include <stdio.h>

// 집 좌표를 저장하는 구조체
struct Point
{
    int x, y;
};

// 최대 50개 집을 저장하는 구조체 배열 미리 만들기
struct Point house[50];

// 절댓값 계산 함수
int abs(int v) { return v < 0 ? -v : v; }

// 두 집 사이의 거리 계산 함수
int dist(int i, int j)
{
    return abs(house[i].x - house[j].x) + abs(house[i].y - house[j].y);
}

int main(void)
{
    int N, K;
    scanf("%d %d", &N, &K);

    for (int i = 0; i < N; i++)
        scanf("%d %d", &house[i].x, &house[i].y);

    int best = 200000; // 정답 초기화 (조건상 최대 거리 200000)

    // 대피소 1개 선택
    if (K == 1)
    {
        // i번째 집을 대피소로 지정
        for (int i = 0; i < N; i++)
        {
            int far = 0;
            // i번째 집과 h번째 집 사이의 거리를 전부 비교해 가장 먼 거리를 찾는다.
            for (int h = 0; h < N; h++)
            {
                int d = dist(h, i);

                if (d > far)
                    far = d;
            }
            // i번째 집이 대피소일 때 가장 먼 거리의 최솟값을 갱신한다.
            if (far < best)
                best = far;
        }
    }
    // 대피소 2개 선택 (조합 탐색)
    else if (K == 2)
    {
        // i번째 집을 대피소로 지정
        for (int i = 0; i < N; i++)
        {
            // i+1번째 집부터 하나씩 대피소로 추가 지정
            for (int j = i + 1; j < N; j++)
            {
                int far = 0;
                // i, j중 가까운 대피소와 h번째 집 사이의 거리를 전부 비교해 가장 먼 거리를 찾는다.
                for (int h = 0; h < N; h++)
                {
                    // 두 대피소 중 더 가까운 곳까지의 거리
                    int d1 = dist(h, i), d2 = dist(h, j);
                    int d = (d1 < d2 ? d1 : d2);

                    if (d > far)
                        far = d;
                }
                // i, j번째 집이 대피소일 때 가장 먼 거리의 최솟값을 갱신한다.
                if (far < best)
                    best = far;
            }
        }
    }
    // 대피소 3개 선택 (조합 탐색)
    else if (K == 3)
    {
        // i번째 집을 대피소로 지정
        for (int i = 0; i < N; i++)
        {
            // i+1번째 집부터 하나씩 대피소로 추가 지정
            for (int j = i + 1; j < N; j++)
            {
                // j+1번째 집부터 또 하나씩 대피소로 추가 지정
                for (int k = j + 1; k < N; k++)
                {
                    int far = 0;
                    // i, j, h중 가까운 대피소와 h번째 집 사이의 거리를 전부 비교해 가장 먼 거리를 찾는다.
                    for (int h = 0; h < N; h++)
                    {
                        // 세 대피소 중 가장 가까운 곳까지의 거리
                        int d1 = dist(h, i);
                        int d2 = dist(h, j);
                        int d3 = dist(h, k);
                        int d = d1 < d2 ? d1 : d2;
                        if (d3 < d)
                            d = d3;

                        if (d > far)
                            far = d;
                    }
                    // i, j, h번째 집이 대피소일 때 가장 먼 거리의 최솟값을 갱신한다.
                    if (far < best)
                        best = far;
                }
            }
        }
    }

    printf("%d\n", best);
    return 0;
}

// dfs로 푸는 법도 익혀두자.

/*
#include <stdio.h>

struct Point {
    int x, y;
};

struct Point house[50];   // 최대 50개 집
int N, K;
int comb[3];              // 선택된 대피소 인덱스 저장 (최대 3개)
int best = 200000;        // 정답 초기값

// 절댓값
int abs_i(int v) { return v < 0 ? -v : v; }

// 맨해튼 거리 계산
int dist(int i, int j) {
    return abs_i(house[i].x - house[j].x) + abs_i(house[i].y - house[j].y);
}

// 선택된 조합(comb[])으로 가장 먼 집까지의 거리 계산
void evaluate() {
    int far = 0;
    for (int h=0; h<N; h++) {
        int d = 200000;
        for (int i=0; i<K; i++) {
            int c = comb[i];
            int dd = dist(h, c);
            if (dd < d) d = dd;  // 가장 가까운 대피소 선택
        }
        if (d > far) far = d;    // 가장 먼 집 갱신
    }
    if (far < best) best = far;  // 최솟값 갱신
}

// DFS로 조합 생성
void dfs(int depth, int start) {
    if (depth == K) {
        evaluate();
        return;
    }
    for (int i=start; i<N; i++) {
        comb[depth] = i;         // i번째 집 선택
        dfs(depth+1, i+1);       // 다음 인덱스부터 탐색 (중복 방지)
    }
}

int main(void) {
    scanf("%d %d", &N, &K);
    for (int i=0; i<N; i++) {
        scanf("%d %d", &house[i].x, &house[i].y);
    }

    dfs(0, 0);
    printf("%d\n", best);
    return 0;
}
*/