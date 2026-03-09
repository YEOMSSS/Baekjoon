# Authored by : marigold2003
# Date : 2026-03-08
# Link : https://www.acmicpc.net/problem/2573


import sys

input = sys.stdin.readline


# [Summary] 빙산

# 빙산의 각 부분별 높이 정보가 담긴 N*M(<=300)board가 주어진다.
# 높이 0은 바닷물을 의미한다.

# 1년이 지날 때마다 접해 있는 바닷물의 수만큼 높이가 줄어든다.
# 빙산이 두 덩어리 이상으로 분리되는 최초의 시간을 구하시오.

# 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 0을 출력한다.
# 입력은 한 덩어리의 빙산이다. 처음 빙산은 0으로 둘러싸여져 있다.


def main() -> None:

    # [Ideas]

    # 1년이 지날 때마다 사이클 검사를 해야 하는가...

    # 일단 이 문제는 graph가 필요한 느낌은 아니다.
    # 빙산 한칸끼리 영향을 준다기보다 그냥 4방향 바닷물만 세면 되니까.
    # 모든 칸을 확인하여 0이 아니면 바닷물 검사를 하면 된다.
    # 근데 모든 칸이 동시에 녹기 때문에 칸을 하나씩 바꾸면 안 되겠구만.

    # 그러면 1년이 지날 때마다 사이클 순회를 해도 되겠구나.
    # padding이 된 채로 입력이 들어온다. 아주 편안하군

    ##########

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    is_zero = [[False] * M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if board[r][c]:
                continue
            is_zero[r][c] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    year = 0

    # 빙산이 한 덩어리면 True 반환
    def dfs(sr, sc, is_zero):
        stack = []
        visited = [row[:] for row in is_zero]
        stack.append((sr, sc))

        while stack:
            r, c = stack.pop()
            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if visited[nr][nc]:
                    continue
                stack.append((nr, nc))

        for row in visited:
            if False in row:
                return False

        return True

    while True:
        year += 1

        temp = set()
        for r in range(1, N - 1):
            for c in range(1, M - 1):

                curr = board[r][c]
                if not curr:
                    continue

                count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_zero[nr][nc]:
                        count += 1

                board[r][c] = max(0, curr - count)
                if not board[r][c]:
                    temp.add((r, c))

        for r, c in temp:
            is_zero[r][c] = True

        # 빙산 분리 확인 dfs
        flag = False
        for r in range(1, N - 1):
            for c in range(1, M - 1):

                # 0은 확인할 필요 없음
                if is_zero[r][c]:
                    continue

                # 한 덩어리가 맞으면 flag는 True
                if dfs(r, c, is_zero):
                    flag = True
                    break
                # 한 덩어리가 아니면 year 출력
                else:
                    print(year)
                    return

            if flag:
                break

        # 여기서 not flag면 전부 0인 것이다.
        if not flag:
            print(0)
            return

    ##########

    return


# [Review]

# 뭔가 실수할 부분이 좀 많은거같음.
# 비효율적으로 짜기도 했고..


if __name__ == "__main__":
    main()
