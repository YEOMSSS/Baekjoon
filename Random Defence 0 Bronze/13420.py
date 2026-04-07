import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    arr = list(input().split())

    match arr[1]:
        case "+":
            result = int(arr[0]) + int(arr[2])
        case "-":
            result = int(arr[0]) - int(arr[2])
        case "*":
            result = int(arr[0]) * int(arr[2])
        case "/":
            result = int(arr[0]) // int(arr[2])

    if result == int(arr[4]):
        print("correct")
    else:
        print("wrong answer")
