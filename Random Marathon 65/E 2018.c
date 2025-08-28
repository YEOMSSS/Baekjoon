/*
a부터 m개의 연속된 자연수들을 더하면 n을 만들 수 있다고 합시다.
그 m개의 자연수들에서 전부 a씩 빼면 0, 1, 2, 3, ..., m-1 이 될 것이고,
그 합은 m(m-1)/2 이므로 n = am + m(m-1)/2 입니다.
즉, 어떤 자연수 m을 골랐는데 1부터 m-1까지의 합을 n에서 뺀 결과가 0 또는 m의 양의 배수이면 됩니다.
m-1까지의 합을 m까지의 합으로 바꾸기 위해 +m -m을 한 후 m까지의 합을 좌변으로 넘기면 n - m(m+1)/2 = (a-1)m.
*/

/*
#include <stdio.h>

int main(void) {
    int N;
    scanf("%d", &N);

    int cnt = 0;
    long long sum = 0; // sum = m(m+1)/2. N이 천만까지니까 sum은 longlong으로 넉넉하게
    for (int m = 1; m <= N; m++) {
        sum += m;

        if ((N - sum) >= 0 && (N - sum) % m == 0) {
            cnt++;
        }
    }

    printf("%d", cnt);

    return 0;
}
*/

// 아니 씨,,, 수학이야?
// 두 포인터로 풀 수 있다고?

#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    // 시작점과 끝점 모두 1에서 시작하자.
    int start = 1, end = 1;
    int sum = 1; // 처음엔 1~1로 1뿐이니 sum도 1에서 시작.
    int cnt = 0;

    while (start <= N) {
        // 합이 목표보다 작으면 end++ (오른쪽 한칸 늘리기)
        if (sum < N) {
            end++; // 오른쪽에 숫자 하나 붙이고
            sum += end; // 그 숫자를 합에 더하기
        }
        // 합이 목표보다 크면 start++ (왼쪽 한칸 줄이기)
        else if (sum > N) {
            sum -= start; // 가장 왼쪽에 있는 숫자를 합에서 빼주고
            start++; // 시작 포인터를 오른쪽으로 한칸 가기
        }
        // 목표에 도달하면 cnt++, start++
        else { // sum == N
            cnt++;
            // 다음 경우를 위해 왼쪽을 줄인다
            sum -= start;
            start++;
        }
    }

    printf("%d", cnt);
    return 0;
}

// 더 직관적이어서 좋다.