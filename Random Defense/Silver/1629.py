# 분할정복은 나중에 다시 해보자.

A, B, C = map(int, input().split())

print(pow(A, B, C))

"""
def pow_mod(a, b, c):
    result = 1
    a = a % c  # 큰 수 방지

    while b > 0:
        if b % 2 == 1:      # b의 현재 비트가 1이면 곱하기
            result = (result * a) % c
        a = (a * a) % c     # 밑을 제곱
        b //= 2             # 지수를 절반으로 줄임

    return result

A, B, C = map(int, input().split())
print(pow_mod(A, B, C))
"""
