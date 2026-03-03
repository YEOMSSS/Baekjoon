# Authored by : marigold2003
# Date : 2026-03-03
# Link : https://www.acmicpc.net/problem/5789


import sys

input = sys.stdin.readline


# [Summary] 한다 안한다

# 0과 1로 이루어진 문자열이 입력된다.
# 양끝이 같으면 한다이고, 다르면 안한다이다.
# 문자열의 길이는 항상 짝수로 주어진다.
# 마지막으로 고르는 두 숫자의 결과를 구하시오.


def main() -> None:

    # [Ideas]

    # 그냥 인덱스로 가운데 둘만 보면 되는거 아니야?

    ##########

    T = int(input())

    for _ in range(T):
        string = input().rstrip()
        mid = len(string) // 2
        print("Do-it" if string[mid] == string[mid - 1] else "Do-it-Not")

    ##########

    return


# [Review]

# 이런 게 힐링이 아닐까?


if __name__ == "__main__":
    main()
