# Authored by : marigold2003
# Date : 2026-03-19
# Link : https://www.acmicpc.net/problem/27648


import sys

input = sys.stdin.readline


# [Summary] 증가 배열 만들기

# N*M(<= 1K) board가 있다.
# 각 칸에 1~K(<= 100K)의 정수를 채워넣어 증가상태로 만들고자 한다.

# 증가상태란 (1, 1)에서 우측하단으로 이동하는 모든 경로가
# 오름차순의 수열을 만듦을 의미한다.


def main() -> None:

    # [Ideas]

    # 뭔가 기믹이 있을 것이다...
    # 좌하로 그은 대각선의 개수를 세면 된다.
    # 그게 K보다 작거나 같으면 성공.
    # 맞는거같은데? 이게 아닐수가없음.

    # 대각선의 개수는 행길이+열길이-1이다.

    # 왼쪽 대각선부터 순서대로 1부터 채워넣으면 된다.
    # 그냥 첫째줄부터 123~, 234~, 345~ 이런식으로 출력해야겠다.

    ##########

    N, M, K = map(int, input().split())

    if (N + M - 1) > K:
        print("NO")
        return

    print("YES")
    for i in range(1, N + 1):
        print(*range(i, i + M))

    ##########

    return


# [Review]

# 역시 발상만 하면 쉬운 문제다.
# 난이도를 모르는 상태로 풀었다면 좀 더 시간이 걸렸을수도.


if __name__ == "__main__":
    main()
