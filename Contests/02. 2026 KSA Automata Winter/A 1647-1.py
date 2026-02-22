# Authored by : marigold2003
# Date : 2026-02-21
# Link : https://www.acmicpc.net/contest/problem/1647/1


import sys

input = sys.stdin.readline


# [Summary] A번 - 소수가 아닌 수 4

# N개의 정수 중 적어도 둘을 골라 그 최소공배수가 소수가 아니도록 만들어야 한다.
# 그렇게 만들 수 있다면 고른 정수의 수와 그 정수들을 출력하시오.


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def main() -> None:

    # [Ideas]

    # 합성수를 찾아야 하니까, 일단 합성수를 하나 고르면 무조건 합성수고.
    # 소수 2개 골라도 합성수고.
    # 1을 고르면? 다른게 소수가 아니거나 1이 아니면 무조건 합성수고.

    # 소수가 나오는 경우는 1이 엮인 경우뿐이다.
    # 1이 있는데 옆이 소수면 소수.
    # 1이 있는데 옆이 1이면 소수.
    # 1이 있는데 옆에 숫자 2개있다? 그럼 합성수.

    ##########

    N = int(input())
    arr = list(map(int, input().split()))

    primes = []
    not_primes = []

    for x in arr:
        if x == 1:
            continue
        if is_prime(x):
            primes.append(x)
        else:
            not_primes.append(x)

    # 합성수가 있는 경우
    if not_primes:
        print("YES")
        print(2)
        print(not_primes[0], arr[0] if arr[0] != not_primes[0] else arr[1])
        return

    # 서로 다른 소수가 2개 이상 있는 경우
    if len(primes) >= 2:
        print("YES")
        print(2)
        print(primes[0], primes[1])
        return

    # 그 외는 불가능
    print("NO")

    ##########

    return


# [Review]

# 1 이노옴


if __name__ == "__main__":
    main()
