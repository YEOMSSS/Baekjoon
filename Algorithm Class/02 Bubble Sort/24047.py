
# 앞자리가 역전이면 append, 뒷자리가 역전이면 appendleft.

import sys
input = sys.stdin.readline

from collections import deque

def main():
    N, K = map(int, input().split())
    arr_N = list(map(int, input().split()))

    queue = deque()

    # 일단 처음 상태 확인용
    for i in range(N - 1):
        if arr_N[i] > arr_N[i + 1]:
            queue.append(i)

    cnt = 0
    while queue:
        cnt += 1
        current = queue.popleft()
        arr_N[current], arr_N[current + 1] = arr_N[current + 1], arr_N[current]

        if current < N - 2 and arr_N[current + 1] > arr_N[current + 2]:
            if not queue or queue[0] != current + 1:
                queue.appendleft(current + 1)

        if 0 < current and arr_N[current - 1] > arr_N[current]:
            queue.append(current - 1)

        if cnt == K:
            # 출력 형식만 달라짐.
            print(*arr_N)
            return

    print(-1)


if __name__ == "__main__":
    main()
