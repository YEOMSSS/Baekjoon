
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

result = arr_A + arr_B

print(*sorted(result))

# 파이썬에선 존나게 쉬운 문젠데. 그치?
