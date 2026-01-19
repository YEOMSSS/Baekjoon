import sys

input = sys.stdin.readline


def main():
    while True:
        n = int(input())
        if n == 0:
            break

        words = [input().rstrip() for _ in range(n)]

        # 비교할 때만 소문자로 비교됨.
        # min(list)는 list에서 가장 작은 값을 반환하지?
        # min(list, key=함수)를 하면 비교 기준이 함수가 되어 가장 최솟값을 반환한다.
        # 여기서는 문자열이니까 아스키코드 기준으로 비교하게 되는거임.
        print(min(words, key=lambda x: x.lower()))


main()
