import sys

input = sys.stdin.readline


# 9 8 7 6 5
# 2 3 4 5 6
# 7 5 3 1 0 16

# 9 8 7 6 5
# 6 5 4 3 2
# 3 3 3 3 3 15

# 버려지는게 없게 하는 것보다
# 가장 큰거에서 가장 작은걸 빼는게 더 벌리네.


def main():

    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))

    # 만족도는 내림차순, 비용은 오름차순 정렬
    As.sort(reverse=True)
    Bs.sort()

    total_customer_satisfatcion_level = 0
    for i in range(min(N, M)):
        current = As[i] - Bs[i]
        # 음수일 때를 빼먹지 말자.
        if current <= 0:
            break
        total_customer_satisfatcion_level += current

    print(total_customer_satisfatcion_level)


if __name__ == "__main__":
    main()
