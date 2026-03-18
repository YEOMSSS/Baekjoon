# Authored by : marigold2003
# Date : 2026-03-12
# Link : https://www.acmicpc.net/problem/23815


import sys

input = sys.stdin.readline


# [Summary] 똥게임

# 사람 1명으로 시작한다.
# N(<= 100K)번의 턴이 주어지며, 각 턴마다 4개의 선택지 중 2개가 주어진다.
# 그 중 하나를 선택한다. (+x -x *x //x)
# 1회에 한해 광고를 보고 선택지를 건너뛸 수 있다. 광고를 보지 않아도 된다.
# 사람의 수를 최대로 만드시오.


def main() -> None:

    # [Ideas]

    # 시뮬레이션이 가능할까?
    # 100K*100K 에바임. 다 하나씩 빼보는건 안된다.

    # 순서대로 진행이 되는 거니까, 중복흐름을 반복할 필요는 없고...
    # 이거, dp구나.

    # 두 칸을 만들어서 광고소모안함, 광고소모함으로 만들자.
    # 광고소모안함은 앞칸 광고소모안함 가져오면 되고
    # 광고소모함은 앞칸 광고소모함 가져오거나 나를 건너뛰자.

    # 게임종료는 중간에 될 수도 있다.
    # dp 안에 음수밖에 없는 타이밍이 생기면 바로 끊자.

    # 아, 앞칸이 음수면 그 칸에서 이어갈 수가 없구나.
    # 이미 그 경우는 게임오버.

    ##########

    N = int(input())
    # dp[i] = [i칸선택, i칸광고]
    dp = [[0, 0] for _ in range(N + 1)]

    dp[0] = ["1", "1"]

    for i in range(1, N + 1):
        s1, s2 = input().split()

        if int(dp[i - 1][0]) > 0:
            # 광고를 소모하지 않은 경우
            dp[i][0] = str(
                max(
                    int(eval(dp[i - 1][0] + s1)),
                    int(eval(dp[i - 1][0] + s2)),
                )
            )

        if int(dp[i - 1][1]) > 0:
            # 광고를 소모하는 경우
            dp[i][1] = str(
                max(
                    int(dp[i - 1][0]),
                    int(eval(dp[i - 1][1] + s1)),
                    int(eval(dp[i - 1][1] + s2)),
                )
            )

        # 둘 다 0 이하일 때를 처리해야 한다.
        if int(dp[i][0]) <= 0 and int(dp[i][1]) <= 0:
            print("ddong game")
            return

    answer = max(map(int, dp[N]))
    print(answer if answer > 0 else "ddong game")

    ##########

    return


# [Review]

# 쉽게 풀리는 dp문제.
# dp는 문제가... 쉽게 풀었을때 확신이 안섬.
# 하여간!!!

# 그래도 eval덕에 귀찮은 연산구현은 스킵했다.


if __name__ == "__main__":
    main()
