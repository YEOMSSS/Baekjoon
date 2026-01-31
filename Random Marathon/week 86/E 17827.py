import sys

input = sys.stdin.readline

# 일단 사이클이 생기기 전까지 굴린 후
# 그 부분을 넘어가는 순간부터는 사이클로 계산한다.


def main() -> None:
    # 노드개수, 질문횟수, N번이 가리키는 노드
    N, M, S = map(int, input().split())
    snail = tuple(map(int, input().split()))

    # K번째 노드 찾기
    def solve(K):

        # 사이클에 포함 안될경우
        if K < S - 1:
            return snail[K]

        # 사이클에 포함시 mod 이용
        K -= S - 1
        cycle = snail[S - 1 :]
        cycle_len = N - S + 1
        K %= cycle_len

        return cycle[K]

    # 질문 M회
    for _ in range(M):
        K = int(input())
        print(solve(K))


if __name__ == "__main__":
    main()
