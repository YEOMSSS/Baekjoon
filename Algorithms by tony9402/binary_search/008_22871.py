# 아니 이거 왜맞지??

import sys

input = sys.stdin.readline


# 이 값으로 건널 수 있는지 확인
def dfs(arr, val) -> bool:
    length = len(arr)

    stack = []
    visited = [False] * length

    stack.append(0)
    visited[0] = True

    while stack:
        print(stack)
        cur = stack[-1]
        if cur == length - 1:
            return True

        for nei in range(cur + 1, length):
            if visited[nei]:
                continue

            power = (nei - cur) * (1 + abs(arr[cur] - arr[nei]))
            if power > val:
                continue

            stack.append(nei)
            visited[nei] = True
            break

        else:
            cur = stack.pop()

    return False


def b_search(arr, val) -> int:
    left = 0
    right = val

    result = 0
    while left <= right:
        mid = (left + right) // 2

        # 이 값으로 가능하면 더 줄여봐도 된다.
        if dfs(arr, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


def main() -> None:
    N = int(input())
    As = list(map(int, input().split()))

    max_power = 0
    for i in range(N):
        for j in range(i + 1, N):
            max_power = max((j - i) * (1 + abs(As[i] - As[j])), max_power)

    print(b_search(As, max_power))


main()
