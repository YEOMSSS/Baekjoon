import sys

input = sys.stdin.readline


def func(arr, mid):
    count = 0
    for length in arr:
        count += length // mid

    return count


def b_search(arr, val):
    left = 0
    right = max(arr)

    result = 0
    while left <= right:
        mid = (left + right) // 2
        # mid가 0이 되는 경우가 없어야 한다.
        if not mid:
            mid += 1
        cur = func(arr, mid)

        # 이 문제는 최대를 구하는 거라서 left로 계속 돌려야한다.
        # 최우측값을 구한다고 생각하면 된다.
        # 더 많이 쪼개졌다면 더 크게 나눠도된다.
        if cur >= val:
            result = mid
            left = mid + 1
        # 같거나 더 적게 쪼개졌다면 더 작게 나눠야한다.
        else:
            right = mid - 1

    return result


def main():
    K, N = map(int, input().split())
    lines = [int(input()) for _ in range(K)]

    print(b_search(lines, N))


main()
