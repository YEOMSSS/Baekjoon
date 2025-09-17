
import sys
input = sys.stdin.readline

N = int(input())

arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

result = 0
for i in range(N):
    if arr_A[i] <= arr_B[i]:
        result += 1

print(result)

