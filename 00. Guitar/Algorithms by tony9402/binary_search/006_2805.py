def b_search(trees: list, val: int) -> int:
    left = 0
    right = max(trees)

    result = 0
    while left <= right:
        mid = (left + right) // 2
        cur = 0
        for tree in trees:
            if (tree - mid) < 0:
                continue
            cur += tree - mid

        # 원하는 양보다 남았으면 더 크게 잘라도 된다.
        if cur >= val:
            result = mid
            left = mid + 1  # 오른쪽으로 더 가보자.
        else:
            right = mid - 1

    return result


def main() -> None:
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    print(b_search(trees, M))


main()
