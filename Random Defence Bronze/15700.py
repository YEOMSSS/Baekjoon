N, M = map(int, input().split())

result = N * (M // 2)

if M % 2:
    result += N // 2

print(result)
