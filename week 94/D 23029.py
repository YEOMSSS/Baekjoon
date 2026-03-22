# Authored by : marigold2003
# Date : 2026-03-22
# Link : https://www.acmicpc.net/problem/23029


import sys

input = sys.stdin.readline


# [Summary] 시식 코너는 나의 것

# N(<= 100K)개 정수로 이루어진 배열이 주어진다.
# 0에서부터 시작해 N을 향해 가며 값을 선택한다.
# 최대 연속 2칸까지만 선택할 수 있으며, 이후 한 칸을 건너뛰어야 한다.
# 연속 칸에서 두번째 칸은 절반의 값으로 인정된다.
# 선택할 수 있는 최대값을 구하시오.


def main() -> None:

    # [Ideas]

    # 딱봐도 dp죠.

    # 우선 dp[i]는 i칸까지의 최대값을 저장해야 한다.
    # 자신이 첫선택인 경우, 두번째선택인경우, 건너뛴경우.
    # 그렇다면 점화식을 쓸 수 있겠지? 이전칸만 확인하면 되겠다.
    # 초라기 한번 푸니까 실버 dp는 그냥 쉽다. 하..

    ##########

    N = int(input())
    arr = [int(input()) for _ in range(N)]

    # 1선, 2선, pass
    dp = [[0, 0, 0] for _ in range(N + 1)]
    dp[0] = [arr[0], 0, 0]

    for i in range(1, N):
        # 이전이 pass여야 1선가능
        dp[i][0] = dp[i - 1][2] + arr[i]
        # 이전이 1선이어야 2선가능
        dp[i][1] = dp[i - 1][0] + (arr[i] // 2)
        # pass는 언제나 가능, 최댓값을 가져오기
        dp[i][2] = max(dp[i - 1])

    print(max(dp[N - 1]))

    ##########

    return


# [Review]

# dp도 좀만 익숙해지면 참 좋을텐데.
# 근데 괴상한 유형이 나오면 구현부터 막히니 참.


if __name__ == "__main__":
    main()
