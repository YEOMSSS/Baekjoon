
import sys
input = sys.stdin.readline

N = int(input())

A, PA, B, PB = map(int, input().split())

result = 0
answer = (0, 0)

if PA > PB:
    for i in range((N // PA) + 1):
        temp = A * i + B * ((N - (PA * i)) // PB)
        if result < temp:
            result = temp
            answer = (i, ((N - (PA * i)) // PB))

else:
    for i in range((N // PB) + 1):
        temp = B * i + A * ((N - (PB * i)) // PA)
        if result < temp:
            result = temp
            answer = (((N - (PB * i)) // PA), i)

print(*answer)
