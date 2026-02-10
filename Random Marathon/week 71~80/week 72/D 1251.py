import sys

input = sys.stdin.readline


def main():
    string = input().rstrip()
    length = len(string)

    result = ["~"]  # z보다 유니코드상 뒤에 위치한다.
    for i in range(1, length - 1):
        for j in range(i + 1, length):
            result.append(string[:i][::-1] + string[i:j][::-1] + string[j:][::-1])
            result.sort()
            result.pop()

    print(*result)


main()
