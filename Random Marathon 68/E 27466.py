
# -2, -3은 A
# -1 은 자음

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
string = input().rstrip()
len_string = len(string)

check = 0
vowels = "AEIOU"

result = ""

for i in range(N):
    current = string[-(i + 1)]
    
    if not check:
        if current not in vowels:
            result += current
            check += 1
        else:
            continue
    
    elif check == 1 or check == 2:
        if current == "A":
            result += current
            check += 1

    elif M - 3 <= len_string <= N - 3:
        result = string[: M - 3] + result[::-1]
        break
    
    len_string -= 1

if len(result) <= 3:
    print("NO")
else:
    print("YES")
    print(result)
