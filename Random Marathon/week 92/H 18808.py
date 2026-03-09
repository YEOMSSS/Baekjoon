# Authored by : marigold2003
# Date : 2026-03-09
# Link : https://www.acmicpc.net/problem/18808


import sys

input = sys.stdin.readline


# [Summary] 스티커 붙이기

# 스티커가 주어진다.
# 회전시키지 않고 떼어내서 board의 가장 상단 좌측에 붙인다.
# 다른 스티커들도 겹치지 않게 붙일 수 있는 가장 상단 좌측에 붙인다.
# 붙일 수 없다면 90도 회전하여 다시 붙여본다.
# 회전시켰는데도 붙이지 못했다면 버린다.

# board에서 스티커가 붙은 칸의 수를 출력한다.


def main() -> None:

    # [Ideas]

    # 문제가 친절하긴 하다. 어떤 식으로 풀어야 할지도 전부 주어졌다.
    # 이제 내가 할 일은 구현이다. 시뮬레이션을 돌려보자.

    # 최상단 최좌측에 붙여야 (0, 0)부터 붙여보면 될 듯.
    # 조금이라도 겹치면 한칸 이동하자. 스티커 입력이 예쁘게 주어진다.
    # 회전이 몹시 귀찮다. 아!!

    ##########

    N, M, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]

    def compare(sr, sc, R, C, sticker):

        for r in range(R):
            for c in range(C):

                # 둘 다 1이면 바로 종료
                if board[r + sr][c + sc] and sticker[r][c]:
                    return False

        return True

    for _ in range(K):
        R, C = map(int, input().split())
        sticker = [list(map(int, input().split())) for _ in range(R)]

        # 회전해보기
        for _ in range(4):

            flag = False
            for dr in range(N - R + 1):
                for dc in range(M - C + 1):
                    if compare(dr, dc, R, C, sticker):
                        flag = True
                        break
                if flag:
                    break

            # 못 붙이면 회전한다.
            if not flag:
                rotated = []
                for row in zip(*sticker[::-1]):
                    rotated.append(row)
                R, C = C, R
                sticker = rotated
                continue

            # 붙일 수 있으면 붙인다.
            for r in range(R):
                for c in range(C):
                    board[r + dr][c + dc] |= sticker[r][c]
            break

        # 못 붙이면 버린다.

    count = 0
    for row in board:
        count += sum(row)

    print(count)

    ##########

    return


# [Review]

# 구현이 재밌는 문제.
# 수업 가야되는데 큰일났다.


if __name__ == "__main__":
    main()
