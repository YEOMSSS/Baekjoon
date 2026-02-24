# Authored by : marigold2003
# Date : 2026-02-20
# Link : https://www.acmicpc.net/problem/11509


import sys

input = sys.stdin.readline


# [Summary] 풍선 맞추기

# 왼쪽에서 오른쪽으로 일렬로 놓인, 높이가 다른 풍선들이 있다.

# 화살은 선택된 높이 H에서 일자로 날아가고,
# 가던 화살이 풍선을 맞추면 터트리고 높이는 H-1이 되어 계속 날아간다.

# 화살은 왼쪽에서 오른쪽으로 쏜다.
# 모든 풍선을 터트리기 위해 쏴야 하는 화살의 최소 개수를 구하시오.


def main() -> None:

    # [Ideas]

    # 왼쪽에서 풍선을 보면, 풍선 사이의 거리는 의미가 없다.
    # 그냥 같은 높이에 풍선이 몇 개 있는지 배열로 저장해도 될 듯.
    # 아, 근데 순서는 좀 중요할지도. 1이 2 앞에 있으면 2번 쏴야하잖아.

    # 앞에서 쏜 화살의 높이를 다 저장해두고
    # 뒤에 그거에서 -1한게 나오면 터트리자.

    # 풍선이 있는 족족 처리가 가능할듯.
    # 현재 풍선을 터트려야 하면 화살을 쏘고
    # 이미 앞 화살에 의해 터진다면 쏠 필요 없이 화살 높이만 조정하자.

    ##########

    N = int(input())
    it = map(int, input().split())

    count = 0
    heights = [0] * 1_000_001

    for h in it:

        if heights[h]:
            heights[h] -= 1
        else:
            count += 1

        heights[h - 1] += 1

    print(count)

    ##########

    return


# [Review]

# 발상만 하면 뭐
# dict가 더 효율적이긴 하다.


if __name__ == "__main__":
    main()
