# Authored by : marigold2003
# Date : 2026-02-14
# Link : https://www.acmicpc.net/problem/27921


import sys

input = sys.stdin.readline


# [Summary] 동전 퍼즐

# 동전으로 모양을 만들었다.
# 바꿔야 하는 모양이 주어진다.
# 옮겨야 하는 동전의 최소 개수를 구하시오.


def main() -> None:

    # [Ideas]

    # 10*10보드가 최대 입력이다.
    # 브루트포스로 전체 영역을 확인하면 될 듯.

    # 바꿔야 할 모양을 현재 영역의 모든 동전에 가져다대보자.
    # 해서 겹치는 동전의 최댓값을 구해 총 동전에서 빼주면 될 듯.

    ##########

    H1, W1 = map(int, input().split())
    original = list(list(input().rstrip()) for _ in range(H1))

    H2, W2 = map(int, input().split())
    goal = list(list(input().rstrip()) for _ in range(H2))

    # original이 goal과 겹쳐지는 모든 경우를 simulation할 수 있는 board를 생성
    board = (
        [["."] * (W2 * 2 + W1 - 2) for _ in range(H2 - 1)]
        + list(["."] * (W2 - 1) + row + ["."] * (W2 - 1) for row in original)
        + [["."] * (W2 * 2 + W1 - 2) for _ in range(H2 - 1)]
    )

    answer = 0
    # 겹치는 모든 경우의 수
    for r in range(H2 + H1 - 1):
        for c in range(W2 + W1 - 1):

            # 같은 위치에 있는 동전 개수 세기
            count = 0
            for i in range(H2):
                for j in range(W2):
                    if goal[i][j] != "O":
                        continue
                    if board[r + i][c + j] != "O":
                        continue
                    count += 1
            answer = max(answer, count)

    # 원래 동전 개수
    coins = sum(row.count("O") for row in goal)

    print(coins - answer)

    ##########

    return


# [Review]

# 발상은 바로 했는데 구현이 생각보다 좀 걸렸다. 35분이라니...
# 인덱스 실수 안하려면 역시 그림을 그려보는게 최고.
# 와 내가 골드5주니까 실버1에서 골드5로 레벨이 올라버리네. 이건 또 처음이네 ㅋㅋㅋㅋㅋ


if __name__ == "__main__":
    main()
