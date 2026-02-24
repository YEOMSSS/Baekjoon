# 1을 이용해서 1, 11
# 11을 이용해서 111, 1111
# 12를 이용해서 121, 1221
# 이런식으로 반쪽만 만들어서 붙이면 된다.

import sys

input = sys.stdin.readline


def main() -> None:
    N = int(input())

    count = 0

    # 1~99999까지 확인하면 된다.
    for i in range(1, 100000):

        # 여기서도 뒤집어줘야 한다.
        if int(str(i) + str(i)[:-1][::-1]) <= N:
            count += 1
        else:
            break

        if int(str(i) + str(i)[::-1]) <= N:
            count += 1

    print(count)


main()
