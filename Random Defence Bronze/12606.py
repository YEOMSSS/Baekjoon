# Authored by : marigold2003
# Date : 2026-02-18
# Link : https://www.acmicpc.net/problem/12606


import sys

input = sys.stdin.readline


# [Summary] Reverse Words (Large)

# 문장이 주어진다.
# 단어의 순서를 거꾸로 출력하시오.


def main() -> None:

    # [Ideas]

    # [::-1]로 날먹하자.
    # 12605와 동일.

    ##########

    T = int(input())

    for i in range(T):
        string = list(input().split())
        string = " ".join(string[::-1])

        print(f"Case #{i + 1}: {string}")

    ##########

    return


# [Review]

# 쉽고 빠르게 푸는 자료구조


if __name__ == "__main__":
    main()
