import sys

input = sys.stdin.readline


# 곱하기를 최대한으로 사용하면 된다.
# 묶어서 생각하지 말고, 각각의 숫자에 대해서 곱하기 횟수와 더하기 횟수를 구해보자.
# 곱하기는 전부 동시에 굴릴 수 있으니 최댓값을 구하고, 더하기는 다 더해주면 되겠다.


# 비트마스킹으로 이진수를 그대로 읽는 경우
# 길이-1 만큼 곱하고, 1의 개수만큼 더한다.
# 11 = 1011 더하고 곱하고 곱하고 더하고 곱하고 더하면 11
# 이진수를 msb부터 1이면 더하고, 다음비트로 갈때마다 곱하는 느낌이 된다.


def main() -> None:
    N = int(input())
    arr = list(map(int, input().split()))

    if not sum(arr):
        print(0)
        return

    plus = 0
    mult = 0

    for v in arr:
        plus += v.bit_count()
        mult = max(mult, v.bit_length())

    print(plus + mult - 1)


if __name__ == "__main__":
    main()


# 반복문을 사용하여 곱하기를 탐욕스럽게 집는 경우

# def main() -> None:
#     N = int(input())
#     arr = list(map(int, input().split()))

#     plus = 0
#     mult = 0

#     for v in arr:

#         mult_temp = 0

#         while v:
#             # 짝수면 2로 나누고, 홀수면 1을 뺀다.
#             if v % 2 == 0:
#                 mult_temp += 1
#                 v //= 2
#             else:
#                 plus += 1
#                 v -= 1

#         mult = max(mult, mult_temp)

#     print(plus + mult)


# if __name__ == "__main__":
#     main()
