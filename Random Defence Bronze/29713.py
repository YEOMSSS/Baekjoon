# Authored by : marigold2003
# Date : 2026-02-25
# Link : https://www.acmicpc.net/problem/29713


import sys

input = sys.stdin.readline


# [Summary] 브실이의 띠부띠부씰 컬렉션 🍪

# input받은 string을 재배열해서 "BRONZESILVER"를 몇 개 만들 수 있는지 구하시오.


def main() -> None:

    # [Ideas]

    # E가 두번나오는거같은데?
    # //2로 따로 처리가 필요해보인다.

    # R도 두개였네 ㅋㅋ
    # 실수하지 않게 Counter를 이용하는 게 좋겠다.

    ##########

    from collections import Counter

    target = Counter("BRONZESILVER")

    counter = {key: 0 for key in target.keys()}

    N = int(input())
    string = input().rstrip()

    for ch in string:
        if ch in counter:
            counter[ch] += 1

    for key, value in target.items():
        counter[key] //= value

    print(min(counter.values()))

    ##########

    return


# [Review]

# dictionary 사용 익숙해지기


if __name__ == "__main__":
    main()
