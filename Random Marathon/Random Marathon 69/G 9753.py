import sys

input = sys.stdin.readline

N = 100_000
sieve = [True] * (N + 1)
sieve[0] = sieve[1] = False

prime_numbers = []
for i in range(2, N + 1):
    if sieve[i]:
        prime_numbers.append(i)
        for j in range(i * i, N + 1, i):
            sieve[j] = False


mults = []
for i in prime_numbers:
    for j in prime_numbers:
        # 예제에서 100001이라는 소수곱이 있다고 줬다.
        if i != j and i * j <= 100_001:
            mults.append(i * j)
        else:
            # 이게 포인트다.
            break

mults.sort()

T = int(input())
for _ in range(T):

    K = int(input())
    for i in mults:
        if i >= K:
            print(i)
            break
