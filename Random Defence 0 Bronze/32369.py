# Authored by : marigold2003
# Date : 2026-11-27
# Link : https://www.acmicpc.net/problem/32369


import sys

input = sys.stdin.readline


# [Summary] 양파 실험

# 칭찬하면 칭찬양파가 A만큼, 비난하면 비난양파가 B만큼 자란다.
# 비난양파가 더 길면 둘의 역할을 바꾼다.
# 둘이 길이가 같으면 비난양파를 1 자른다.
# 이 짓을 매일매일 하고 실험 결과를 출력하시오. 누가 더 기냐?


def main() -> None:

    # [Ideas]

    # 그대로 구현해 보자. 시뮬레이션.

    ##########

    N, A, B = map(int, input().split())

    OA, OB = 1, 1
    for _ in range(N):
        OA += A
        OB += B

        if OA == OB:
            OB -= 1

        elif OB > OA:
            OA, OB = OB, OA

    print(OA, OB)

    ##########

    return


# [Review]

# 간단한 시뮬레이션.
# 비난 양파는 잘 자란다.


if __name__ == "__main__":
    main()
