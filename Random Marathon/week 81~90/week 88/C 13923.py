# Authored by : marigold2003
# Date : 2026-02-06
# Link : https://www.acmicpc.net/problem/13923

import sys

input = sys.stdin.readline


# [Summary] 오버워치 월드컵

# N*N 보드가 N종류 알파벳으로 채워져서 들어온다.
# 각 행과 각 열 내에 겹치는 알파벳은 존재하지 않아야 한다.
# 잘못 입력된 값을 찾아 올바르게 고쳐라.


def main() -> None:

    # [Ideas]

    # 일단 모든 행의 set을 비교한다.
    # 다르게 되어 있는 set을 뱉은 열을 확인한다.
    # 그 열의 set을 확인해 올바르게 고친다.

    ##########

    while True:

        # EOF 입력 확인
        N = input()
        if not N:
            return

        N = int(N)
        board = tuple(tuple(input().rstrip()) for _ in range(N))

        # 0행과 1행의 구성이 같으면 저장
        if set(board[0]) == set(board[1]):
            correct_set = set(board[0])
        # 다르다면 2행은 무조건 올바르다.
        else:
            correct_set = set(board[2])

        # 모든 행에 대하여 검사 시작
        for r, row in enumerate(board):
            # 정상적인 행은 통과
            if set(row) == correct_set:
                continue

            # 들어갈 수 없는 알파벳이 들어가 있는 경우
            for c, ch in enumerate(row):

                # 정상적인 알파벳은 통과
                if ch in correct_set:
                    continue

                # 들어갈 수 없는 알파벳의 좌표를 출력
                print(r + 1, c + 1, *(correct_set - set(row)))
                break

            else:
                # 들어갈 수 있는 팀이지만, 2회 반복되는 경우
                from collections import Counter

                # Counter로 2회 등장하는 값 찾기
                wrong = Counter(row).most_common(1)[0][0]

                # wrong을 가진 두 열에 대해 각각 확인
                for c, ch in enumerate(row):

                    # wrong을 가지지 않은 정상적인 열은 통과
                    if ch != wrong:
                        continue

                    # wrong을 가졌으나 정상적인 열은 통과
                    if set(board[i][c] for i in range(N)) == correct_set:
                        continue

                    # 행과 열이 모두 비정상인 경우 wrong의 좌표를 출력
                    print(r + 1, c + 1, *(correct_set - set(row)))
                    break

    ##########

    return


# [Review]

# set 연산과 구현
# 더 간단히 짤 수 있겠지만, 생각나는대로 가볍게 짜본다.

if __name__ == "__main__":
    main()
