'''
import sys
input = sys.stdin.readline

arr = input().rstrip()

prev = ""
happy = 0
sad = 0

for char in arr:

    if char == ":":
        prev = ":"

    elif prev == ":":
        if char == "-":
            prev = "-"
        else:
            prev = ""

    elif prev == "-":
        if char == ")":
            happy += 1
            prev = ""
        elif char == "(":
            sad += 1
            prev = ""
        else:
            prev = ""

    else:
        continue

if happy == sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
elif happy < sad:
    print("sad")

# 이걸 c언어로 할 수 있겠지? 도전이다.
'''

import sys
input = sys.stdin.readline

arr = input().rstrip()

happy = 0
sad = 0

for i in range(len(arr) - 2):
    if arr[i] == ':' and arr[i + 1] == '-':
        if arr[i + 2] == '(':
            sad += 1
        elif arr[i + 2] == ')':
            happy += 1

if happy == sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
elif happy < sad:
    print("sad")
