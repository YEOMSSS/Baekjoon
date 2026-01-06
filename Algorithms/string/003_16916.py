import sys

input = sys.stdin.readline


# 파이썬 지리네, 문자열 길이 백만인데도 처리가 된다고??
def main() -> None:
    string = input().rstrip()
    P = input().rstrip()

    print(1 if P in string else 0)


main()
