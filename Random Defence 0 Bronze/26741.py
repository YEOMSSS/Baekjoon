# Authored by : marigold2003
# Date : 2026-02-04
# Link : https://www.acmicpc.net/problem/26741

import sys

input = sys.stdin.readline


# [Summary]

# 닭과 소가 있다.
# 머리는 다 하나씩 있다. 그래야지
# 닭은 다리가 두개고 소는 다리가 네개다.
# 총 머리와 다리 개수가 주어질 때 닭과 소가 각각 몇 마리인지 구하여라.


def main() -> None:

    # [Ideas]

    # 동물수 * 2를 해서 일단 다 닭다리라고 치면
    # (다리수 - 동물수*2) // 2 만큼 소가 있을 것이다.
    # 그럼 그걸 다시 동물수에서 빼면 될 듯.

    ##########

    # 머리수, 다리수
    H, L = map(int, input().split())
    cow = (L - (H * 2)) // 2
    print(H - cow, cow)

    ##########

    return


# [Review]

# 나도 머리가 하나고, 나도 다리가 두개지롱.
# 근데 이게 11006이랑 같다고?

if __name__ == "__main__":
    main()
