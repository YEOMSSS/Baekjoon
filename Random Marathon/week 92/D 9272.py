# Authored by : marigold2003
# Date : 2026-03-06
# Link : https://www.acmicpc.net/problem/9272


import sys

input = sys.stdin.readline


# [Summary] 상근이의 아이디어

# 정수 a, b가 있다. b는 a보다 크다. (<= 10K)
# p(n) = 2**n 이다.
# S(a, b)는 a이상 b이하인 모든 정수 n의 p(p(n))+1 = 2**(2**n)+1 의 집합이다.
# T(a, b)는 S(a, b)의 원소를 둘씩 짝지어 만드는 (c, d)의 집합이다. (c < d)
# R(a, b)는 T(a, b) 속 (c, d)의 gcd의 총합이다.
# a, b가 주어졌을 때, R(a, b)를 구하시오.


def main() -> None:

    # [Ideas]

    # 문제 해석하는게 일이네;;
    # 일단 p(p(n))+1은 너무 크다. gcd를 바로 구하는 과정이 필요함.
    # 근데 그거 아냐? 저 gcd는 전부 1이라는거.

    # 이건 페르마 수였던 것이다. 아! 하!
    # 모든 페르마 수는 쌍소관계라는거임.
    # 이러면 문제가 갑자기 확 쉬워진다. 그냥 조합 수 찾기 문제가 되어버린다.

    # 그냥 (b - a + 1)(b - a) / 2 가 되어버렸다. 개쉽네?

    ##########

    a, b = map(int, input().split())
    print((b - a + 1) * (b - a) // 2)

    ##########

    return


# [Review]

# 수가 너무 크다는 건, 타개할 쉬운 방법이 존재한다는 의미.
# 이 앞, 함정 있음 과 같은 의미로 인식하면 된다.


if __name__ == "__main__":
    main()
