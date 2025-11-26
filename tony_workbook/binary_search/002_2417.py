def main() -> None:
    N = int(input())

    left = 0
    right = int(N**0.5) + 10

    answer = 0
    while left <= right:
        mid = (left + right) // 2
        cur = mid**2

        # 항상 right를 먼저 처리할 것. 그걸 잊지 않을 것.
        if cur >= N:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


main()
