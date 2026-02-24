import sys

input = sys.stdin.readline


# from math import gcd


def Euclidean(a, b):

    # 나머지가 0이 되면 종료
    while b:
        a, b = b, a % b

    return a


def main() -> None:
    while True:
        decimal = input().rstrip()
        if not decimal:
            return

        point = decimal.find(".")
        parenthesis = decimal.find("(")

        # 정수부, 비순환부, 순환부
        integer_part = decimal[:point]
        non_repeating_part = decimal[point + 1 : parenthesis]
        repeating_part = decimal[parenthesis + 1 : -1]

        only_numbers = integer_part + non_repeating_part + repeating_part

        # 분자, 분모
        numerator = int(only_numbers) - int(
            only_numbers[: len(integer_part) + len(non_repeating_part)]
        )
        denominator = int("9" * len(repeating_part) + "0" * len(non_repeating_part))

        fraction_gcd = Euclidean(numerator, denominator)
        numerator //= fraction_gcd
        denominator //= fraction_gcd

        print(f"{decimal} = {numerator} / {denominator}")


if __name__ == "__main__":
    main()
