def main() -> None:

    N = int(input())
    K = int(input())

    sieve = [0] * (N + 1)

    for i in range(2, N + 1):
        if sieve[i]:
            continue
        for j in range(i, N + 1, i):
            sieve[j] = i

    count = 0
    for i in range(1, N + 1):
        if sieve[i] > K:
            continue
        count += 1
    print(count)


main()


# 시간초과나는코드.
"""
def main() -> None:

    N = int(input())
    K = int(input())

    primes = []

    sieve = [True] * (N + 1)
    # sieve[0], sieve[1] = False, False

    for i in range(2, int(N**0.5) + 1):
        if not sieve[i]:
            continue
        for j in range(i * i, N + 1, i):
            sieve[j] = False

    for i in range(N, 1, -1):
        if not sieve[i]:
            continue
        primes.append(i)

    count = 0
    for i in range(1, N + 1):

        max_prime = K + 1

        for p in primes:
            if p > i:
                continue

            if not i % p == 0:
                continue

            max_prime = p
            break

        if max_prime <= K:
            count += 1

    print(count + 1)


main()
"""
