T = int(input())

result = []
result.append(T // 300)
T %= 300
result.append(T // 60)
T %= 60
result.append(T // 10)
T %= 10

if not T:
    print(*result)
else:
    print(-1)
