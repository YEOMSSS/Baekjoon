import sys

input = sys.stdin.readline


def main() -> None:
    N = int(input())
    towers = list(map(int, input().split()))

    stack = []
    result = [0] * N
    for i, h in enumerate(towers):

        while stack:
            cur = stack[-1]

            # 더 작은 경우는 의미없으므로 제거
            if cur[1] < h:
                stack.pop()

            # 더 큰 경우 벽에 닿았다.
            else:  # cur[1] > h
                result[i] = cur[0] + 1
                break

        stack.append((i, h))
        # print(stack)

    print(*result)


main()
