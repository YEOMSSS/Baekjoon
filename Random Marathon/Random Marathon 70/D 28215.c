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
