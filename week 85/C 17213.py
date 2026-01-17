import sys

input = sys.stdin.readline

from math import comb


# 일단 전부 하나씩은 고르고 시작하니 M-N개만 찾으면 된다.
# ★ ★ | ★ | ★ ★ 별과 막대. 막대기 위치만 정하면 된다.
def main() -> None:
    N = int(input())
    M = int(input())

    # 별과 막대가 모두 놓일 수 있는 칸은 M-N + N-1이다.
    # 막대를 어느 칸에 놓을지 정하면 된다.
    print(comb((M - N) + N - 1, N - 1))


if __name__ == "__main__":
    main()
