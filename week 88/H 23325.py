# Authored by : marigold2003
# Date : 2026-02-08
# Link : https://www.acmicpc.net/problem/23325


import sys

input = sys.stdin.readline


# [Summary] 마법천자문

# 수는 +- 11, + 10, - 1 이렇게 3가지
# 부호는 + 더하기, - 빼기 이렇게 2가지

# 수식의 최대 길이는 20만이다.
# 수, 부호, 수, 부호, ..., 수의 형태로 이루어진다.


def main() -> None:

    # [Ideas]

    # 이걸 브루트포스로 풀 수 있을까?
    # 분기는 +-를 만났을 때마다 생긴다.
    # 재귀로 들어가게 되면 2의 +-개수제곱이 될 듯. 너무 많아

    # 아마 dp가 될 것 같다. 점화식이 어떻게 될까?
    # 부호가 있는 칸을 어떤 식으로 처리할지 고민이 된다.
    # dp에 칸을 2개 만들어서 현재 칸이 숫자일 때, 현재 칸이 부호일 때로 나눠서 쓰자.

    # +----+-+-
    # (10, 0), (11, 10), (9, 11), (10, 9), (8, 10), (0, 8), ((-1, 9), 0), (-10, 9), ((-11, 10), -10)

    # +일때 앞칸의 부호부분을 앞칸 부호에 맞춰 계산해 현재칸 수부분에 넣기
    # +일때 앞칸의 수부분을 현재칸 부호부분에 넣기

    # -일때 앞칸이 +면 앞칸 수부분에 앞앞칸 부호에 맞춰 1을 계산해 현재칸 수부분에 넣기
    # -일때 앞칸의 부호부분을 앞칸 부호에 맞춰 계산해 현재칸 수부분에 넣기
    # -일때 앞칸의 수부분을 현재칸 부호부분에 넣기

    # 헷갈린다. 일단 만들어보자.

    ##########

    expression = list(input().rstrip())

    for i, e in enumerate(expression):
        if e == "+":
            expression[i] = 10
        else:
            expression[i] = 1

    length = len(expression)
    if length == 1:
        print(expression[0])
        return
    if length == 2:
        print(11)
        return

    dp = [[-1000000, -1000000] for _ in range(length)]
    dp[0][0] = expression[0]
    dp[1][1] = dp[0][0]
    if expression[:2] == [10, 1]:
        dp[1][0] = 11

    for i in range(2, length):
        curr = expression[i]

        # +의 경우
        if curr == 10:
            dp[i][1] = dp[i - 1][0]

            if expression[i - 1] == 10:
                dp[i][0] = dp[i - 1][1] + curr

            else:
                dp[i][0] = dp[i - 1][1] - curr

        # -의 경우
        if curr == 1:
            dp[i][1] = dp[i - 1][0]

            if expression[i - 1] == 10:
                if expression[i - 2] == 10:
                    dp[i][0] = dp[i - 1][0] + 1
                else:
                    dp[i][0] = dp[i - 1][0] - 1

                dp[i][0] = max(dp[i][0], dp[i - 1][1] + curr)

            else:
                dp[i][0] = dp[i - 1][1] - curr

    print(dp[length - 1][0])

    ##########

    return


# [Review]

# dp 진짜 벽이네
# 재밌긴 한데 진짜 에바네

if __name__ == "__main__":
    main()
