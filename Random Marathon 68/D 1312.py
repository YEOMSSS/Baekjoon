
A, B, N = map(int, input().split())

# N - 1 회 반복한 후
for _ in range(N - 1):
    A = (A * 10) % B

# 여기서 마지막 한번.
print((A * 10 // B) % 10)