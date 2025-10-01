
import sys
input = sys.stdin.readline

K = int(input())
string = input().rstrip()

arr = []

check = True
for i in range(len(string) // K):
    if check:
        arr.append(string[i * K : (i + 1) * K])
        check = False
    else:
        arr.append(string[i * K : (i + 1) * K][::-1])
        check = True

for i in range(K):
    for j in range(len(string) // K):
        print(arr[j][i], end= "")


