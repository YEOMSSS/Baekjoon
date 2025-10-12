'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

num_list = list(map(int, input().split()))

pointer_A = 0
pointer_B = K

total = 0

for i in range(K):
    total += num_list[i]
    result = total

while pointer_B < N:
    total -= num_list[pointer_A]
    total += num_list[pointer_B]
    
    pointer_A += 1
    pointer_B += 1

    if total > result:
        result = total

print(result)
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

num_list = list(map(int, input().split()))

total = sum(num_list[:K])
answer = total
for i in range(N - K):
    total = total - num_list[i] + num_list[i + K]
    answer = max(total, answer)

print(answer)
