import sys

input = sys.stdin.readline


def b_search(budgets: list, val: int) -> int:
    left = 0
    right = val

    result = 0
    while left <= right:
        mid = (left + right) // 2
        cur = 0
        for b in budgets:
            if b < mid:
                cur += b
            else:
                cur += mid

        # 예산보다 적으면 키워도 된다.
        if cur <= val:
            result = mid
            left = mid + 1
        # 예산을 넘으면 줄여야만 한다.
        else:
            right = mid - 1

    if result >= sum(budgets):
        result = max(budgets)
    return result


def main() -> None:
    N = int(input())
    budgets = list(map(int, input().split()))
    target = int(input())

    print(b_search(budgets, target))


main()
