
N, K = map(int, input().split())

list = [int(input()) for _ in range(N)]

visited = [False] * N

stack = [0]

cnt = 0

while stack:
    current = stack.pop()

    if current == K:
        print(cnt)
        break
    if visited[current]:
        print(-1)
        break

    cnt += 1
    stack.append(list[current])
    visited[current] = True

# 죨라 쉬운 dfs
        