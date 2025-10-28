"""
import sys

input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

len_s = len(s)
len_t = len(t)


def compare(i):
    # 파이썬 슬라이싱은 인덱스가 초과되어도 안전하다.
    if s == t[i : i + len_s]:
        if i + len_s == len_t:
            return 1
        # elif i + len_s > len_t:
        #     return 0
        return compare(i + len_s)
    else:
        return 0


print(compare(0))
"""

import math

s = input()
t = input()

s_len = len(s)
t_len = len(t)

LCM = math.lcm(s_len, t_len)

s_len = LCM // s_len
t_len = LCM // t_len

if s * s_len == t * t_len:
    print(1)
else:
    print(0)

# 문제를 잘 읽자.
