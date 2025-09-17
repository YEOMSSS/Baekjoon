
import sys
input = sys.stdin.readline

N = int(input())

large = 0
small = 0

for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a

    large = max(large, a)
    small = max(small, b)

print(large * small)
