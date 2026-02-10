import math


def main():

    T = int(input())

    for _ in range(T):

        c = int(input())

        a, b = map(float, input().split())

        if c == 1:
            r = (a**2 + b**2) ** 0.5
            t = math.atan2(b, a)
            if t < 0:
                t += math.pi * 2
            print(f"{r:.7f} {t:.7f}")

        if c == 2:
            x = a * math.cos(b)
            y = a * math.sin(b)
            print(f"{x:.7f} {y:.7f}")


main()
