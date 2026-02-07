# Authored by : marigold2003
# Date : 2026-02-07
# Link : https://www.acmicpc.net/problem/26651

import sys

input = sys.stdin.readline


# [Summary]

# 그램팬인 부분문자열의 개수가 X개인 문자열 S를 찾아보자.
# 문자열 S는 100_000을 넘지 않는다. X는 최대 1_000_000_000


def main() -> None:

    # [Ideas]

    # 부분문자열은 연속된 인덱스다.
    # 그러면 조절이 가능한 건 A나 Z뿐이다.

    # ABCDEFGHIJKLMNOPQRSTUVWXYZ는 고정으로 둔다.
    # 앞에 A를 붙이면 AAZ, AZ가 된다.
    # 앞에 A를 2개 붙이면 AAAZ, AAZ, AZ가 된다.
    # A하나 Z하나 하면 AAZZ, AAZ, AZZ, AZ가 된다.

    # A개수 * Z개수를 하면 개수가 나올 것.

    # 어라? 가까운 약수쌍 찾기로는 이 문제가 풀리지 않는다.
    # 999999999는 2997 333667... 이러면 안 된다.

    # 문자열 2개를 합치는 방향으로 가보자...
    # AAZAZ가 되면 2+1 = 3개.

    # 최대한 적게 쓰는 걸로 끊어가는게 좋겠지?
    # 웬만하면 제곱수를 우선적으로 사용해야겠다.

    ##########

    X = int(input())

    if not X:
        print("THEBATTLECATS")
        return

    # X보다 작은 가장 큰 제곱수로 계속 문자열을 붙인다.
    while X:

        curr = int(X**0.5)

        print("A" * curr + "BCDEFGHIJKLMNOPQRSTUVWXY" + "Z" * curr, end="")

        X -= curr**2

    ##########

    return


# [Review]

# 역시 대놓고 쉬운 문제는 아니었다.
# 약수만 가지고 풀 수 있었으면 이게 실버였겠지

if __name__ == "__main__":
    main()
