import sys

input = sys.stdin.readline


def is_palindrome(x):
    L = x.bit_length()

    # 비트를 양끝에서부터 한칸씩 오면서 다른지 같은지 확인
    for i in range(L // 2):
        left = (x >> (L - 1 - i)) & 1
        right = (x >> i) & 1

        if left != right:
            return False

    return True


def func():
    X = int(input())

    cnt = 0
    while True:

        if is_palindrome(X + cnt):
            print(cnt)
            return

        if X - cnt > 0 and is_palindrome(X - cnt):
            print(cnt)
            return

        cnt += 1


def main():
    T = int(input())

    for _ in range(T):
        func()


if __name__ == "__main__":
    main()
