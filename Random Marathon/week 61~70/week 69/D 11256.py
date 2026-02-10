
import sys
input = sys.stdin.readline

def func():
    J, N = map(int, input().split())

    arr = []
    for _ in range(N):
        R, C = map(int, input().split())
        arr.append(R * C)

    arr.sort(reverse= True)

    answer = 0
    for box in arr:
        J -= box
        answer += 1
        if J <= 0:
            break

    print(answer)

def main():
    N = int(input())

    for _ in range(N):
        func()

if __name__ == "__main__":
    main()