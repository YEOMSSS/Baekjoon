import sys

input = sys.stdin.readline

from itertools import combinations


# smallant기준으로 지면-1 비겨면0 이기면1
def judge(l: str, s: str) -> int:
    if l == s:
        return 0
    elif l == "R" and s == "P":
        return 1
    elif l == "P" and s == "S":
        return 1
    elif l == "S" and s == "R":
        return 1
    else:
        return -1


def check(comb, lighter, smallants):
    flag = False
    l = lighter
    for i in comb:
        s = smallants[i]
        result = judge(l, s)

        if result == 1:
            flag = False
            l = s
        elif result == 0:
            if flag:
                return False
            flag = False
        else:
            flag = True
            l = s

    return True


def func(length, lighter, smallants):
    count = 0
    for comb in combinations(range(0, len(smallants)), length):
        if check(comb, lighter, smallants):
            count += 1
    return count


# 앞에서 지고 다음에 비길때만 확인한다.
def main() -> None:
    lighter = input().rstrip()
    smallants = input().rstrip()

    length = len(smallants)
    count = 0

    for i in range(1, length + 1):
        count += func(i, lighter, smallants)

    print(count)


main()
