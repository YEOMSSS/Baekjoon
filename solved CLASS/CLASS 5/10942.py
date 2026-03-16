# Authored by : marigold2003
# Date : 2026-03-16
# Link : https://www.acmicpc.net/problem/10942


import sys

input = sys.stdin.readline


# [Summary] 팰린드롬?

# 자연수 N(<= 2000)개로 이뤄진 배열이 있다.
# S번째에서 E번째까지 수가 팰린드롬인지 아닌지 판단하시오.
# 질문은 M(<= 1M)회 진행된다.


def main() -> None:

    # [Ideas]

    # 질문이 엄청나게 많기 때문에 시뮬레이션으로는 불가능할 것.
    # (S, E)는 2K*2K = 4M개 생성된다.
    # 모든 답을 구해놔야 한다. 구할 수 있어?

    # 2K개의 자연수에 대해 시뮬레이션을 진행해볼까.
    # set에 가능한 경우를 넣어두는거지.
    # 모든 자연수에서 양옆으로 한칸씩 가면서 동일한지 확인하면 될듯?
    # 가운데가 2개인경우도 봐야하지 않나? 좌우동일시도 보자.
    # 그러면 검사가 대충 4K회 진행되겠네.
    # set도 막 엄청 많이 쌓이진 않을거같은데?

    ##########

    N = int(input())
    arr = list(map(int, input().split()))

    result = [[0] * N for _ in range(N)]

    for i in range(N):

        # 홀수개인 경우
        left = i
        right = i
        while left >= 0 and right < N and arr[left] == arr[right]:
            result[left][right] = 1
            left -= 1
            right += 1

        # 짝수개인 경우
        left = i
        right = i + 1
        while left >= 0 and right < N and arr[left] == arr[right]:
            result[left][right] = 1
            left -= 1
            right += 1

    M = int(input())
    for _ in range(M):
        s, e = map(int, input().split())
        print(result[s - 1][e - 1])

    ##########

    return


# [Review]

# 될련지 모르겠네, 일단 조져보자.
# 튜플이랑 set, in은 시간초과네. 배열로 접근하자.


if __name__ == "__main__":
    main()
