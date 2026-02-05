# Authored by : marigold2003
# Date : 2026-02-05
# Link : https://www.acmicpc.net/problem/16208

import sys

input = sys.stdin.readline


# [Summary]

# x + y 쇠막대를 x, y로 나누는 데 필요한 비용은 xy이다.
# a1 + a2 + ... + an 길이의 쇠막대를 a1, a2, ..., an 길이의 쇠막대로 나눈다.
# 쇠막대를 나누는 최소 비용을 구하시오.


def main() -> None:

    # [Ideas]

    # 냄새가 딱 그리디다.
    # 약수를 생각해보면, 1*6이랑 2*3이 있지. 1+6이 2+3보다 크다.
    # 수의 차이가 커질수록 곱이 같을 때 합이 커진다. 합이 같으면 곱이 작아지겠지.

    # 그럼 a1 ~ an을 작은 수부터 정렬해서 잘라내면 된다.
    # 가장 작은 길이가 쇠막대와 차가 가장 크니까.

    ##########

    N = int(input())
    arr = list(map(int, input().split()))
    # arr.sort() 정렬이 필요가 없다고

    length = sum(arr)

    answer = 0
    # 솔직히 [:-1]까지는 필요없긴한데
    for num in arr[:-1]:
        length -= num
        answer += length * num

    print(answer)

    ##########

    return


# [Review]

# 마음이 편안해지는 그리디
# 인 줄 알았는데, 순서가 상관 없다고???

if __name__ == "__main__":
    main()
