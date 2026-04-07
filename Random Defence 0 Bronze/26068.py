# Authored by : marigold2003
# Date : 2026-03-07
# Link : https://www.acmicpc.net/problem/26068


import sys

input = sys.stdin.readline


# [Summary] 치킨댄스를 추는 곰곰이를 본 임스 2

# 유효기간이 90일 이하로 남은 기프티콘만 사용할 것이다.
# 선물받은 횟수 N(<=1K)과 남은 유효기간이 주어진다.

# 임스가 사용할 기프티콘의 개수를 구하시오.


def main() -> None:

    # [Ideas]

    # 입력 즉시 판정하여 카운트
    # 형태가 "D-" + int 이니까 int([2:]) 로 parsing 하자.

    ##########

    N = int(input())
    answer = 0

    for _ in range(N):
        string = input().rstrip()
        if int(string[2:]) <= 90:
            answer += 1

    print(answer)

    ##########

    return


# [Review]

# 이런 문제도 있어야 먹고 살지.


if __name__ == "__main__":
    main()
