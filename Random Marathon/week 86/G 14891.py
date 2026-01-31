import sys

input = sys.stdin.readline

# 하여간 구현은 실수가 많다.
# 내가 어디서 뭘 놓쳤는지 기억이 안난다.

from collections import deque


def main() -> None:
    gears = [deque(map(int, input().rstrip())) for _ in range(4)]

    K = int(input())
    commands = [tuple(map(int, input().split())) for _ in range(K)]

    for g, r in commands:
        # 동일 여부 저장
        # [0]이 12시, [2]가 3시, [6]이 9시
        state = [
            gears[0][2] == gears[1][6],
            gears[1][2] == gears[2][6],
            gears[2][2] == gears[3][6],
        ]

        # 왼쪽 기어 확인
        idx = g - 2
        cnt = 1
        while idx >= 0:
            # 동일하다면 스탑
            if state[idx]:
                break
            gears[idx].rotate(r * ((-1) ** cnt))
            idx -= 1
            cnt += 1

        # 오른쪽 기어 확인
        idx = g
        cnt = 1
        while idx < 4:
            # 동일하다면 스탑
            if state[idx - 1]:
                break
            gears[idx].rotate(r * ((-1) ** cnt))
            idx += 1
            cnt += 1

        gears[g - 1].rotate(r)

    answer = 0
    for i in range(4):
        if gears[i][0]:
            answer += 2**i

    print(answer)


if __name__ == "__main__":
    main()
