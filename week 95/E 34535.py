# Authored by : marigold2003
# Date : 2026-03-25
# Link : https://www.acmicpc.net/problem/34535


import sys

input = sys.stdin.readline


# [Summary] Grid Traveler

# N*N(<= 1K) board를 채워야 한다.
# 1~N*N의 숫자들이 겹치지 않게 board를 채우고 있다.
# 1에서부터 시작해서, i칸을 이동해 i+1로 이동한다.
# 이 이동을 반복해 N*N에 도달할 수 있는지 판단하시오.
# 가능하다면, 가능한 board를 출력하시오.


def main() -> None:

    # [Ideas]

    # 딱봐도 애드혹. 시뮬레이션은 아님.
    # 분명 뭔가 규칙이 있을거임. 묶이는 형태가 있을거같은데.

    # 그 스네이크 게임 있잖아. 그거 사과 하나 먹으면 뒤집히는거.
    # 그거 생각이 나는데...

    # 홀수일때랑 짝수일때랑 모양이 다르다.
    # 보드의 모든 칸을 긋는 경로를 하나 그린다.
    # 그리고 그 중간점을 하나 고른다.
    # 그게 1임.

    # 앞뒤로 3,5,7... 홀수랑 2,4,6...짝수로 진행하면 된다.
    # 홀수면 중심에있고, 짝수면 가장자리에있겠는데.

    # 뒤집힌 홀수배열 + 정렬 짝수배열을
    # 모든 칸을 잇는 경로를 따라 새기면 된다!!
    # 불가능한 경우가 없는거같은데?

    ##########

    N = int(input())
    print("YES")

    nums = list(range(1, N * N + 1, 2))
    nums.reverse()
    nums.extend(list(range(2, N * N + 1, 2)))

    for i in range(N):
        temp = i * N
        if i % 2:
            print(*nums[temp : temp + N])
        else:
            print(*reversed(nums[temp : temp + N]))

    ##########

    return


# [Review]

# 알아내 버린 거야!!!


if __name__ == "__main__":
    main()
