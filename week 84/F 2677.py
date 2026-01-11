import sys

input = sys.stdin.readline

from decimal import Decimal, getcontext, ROUND_FLOOR, ROUND_CEILING

codes = "PQWERTYUIOJ#SZK*?F@D!HNM&LXGABCV"
getcontext().prec = 40


def func() -> None:
    D = Decimal(input())

    if not (Decimal("-1.0") <= D < Decimal("1.0")):
        print("INVALID VALUE")
        return

    # 65536
    scaled = D * (1 << 16)

    if D >= 0:
        n = int(scaled.to_integral_value(rounding=ROUND_FLOOR))
    else:
        n = int(scaled.to_integral_value(rounding=ROUND_CEILING))

    if n < 0:
        n = (1 << 17) + n

    bits = format(n, "017b")

    opcode = int(bits[:5], 2)
    addr = int(bits[5:16], 2)
    t = bits[16]

    print(f"{codes[opcode]} {addr} {'D' if t == '1' else 'F'}")


def main() -> None:
    T = int(input())

    for _ in range(T):
        func()


if __name__ == "__main__":
    main()
