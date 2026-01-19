import sys
from decimal import Decimal, getcontext

input = sys.stdin.readline


def main() -> None:
    A, B = input().split()

    getcontext().prec = 1100  # 계산 정밀도 (출력보다 넉넉하게)
    result = Decimal(A) / Decimal(B)

    print(f"{result:.1001f}")


if __name__ == "__main__":
    main()
