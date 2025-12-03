# 어렵다. dp는 어렵다

import sys

input = sys.stdin.readline


# smallant기준으로 지면-1 비겨면0 이기면1
def check(l: str, s: str) -> int:
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


# 1 1
# 1*2+1 11 01 10
# 3*2+1 111 011 101 110 001 010 100
# 7*2+1 0001, 앞에거에 1이나 0 붙이기


# 앞에서 지고 다음에 비길때만 확인한다. <<<<<<똑바로 잘 써놓고 왜 문제를 이따위로...
def main() -> None:
    lighter = input().rstrip()
    smallants = input().rstrip()

    length = len(smallants)
    dp = [[0, 0] for _ in range(length)]

    dp[0] = [1, check(lighter, smallants[0])]
    lighter = smallants[0]

    for i in range(1, length):
        smallant = smallants[i]
        result = check(lighter, smallant)

        # 이겼을땐 상관없음
        if result == 1:
            lighter = smallant
            dp[i] = [dp[i - 1][0] * 2 + 1, 1]

        # 비겼을땐 앞에서 졌는지 확인
        elif result == 0:
            if dp[i - 1][1] == -1:
                dp[i] = [dp[i - 1][0], 0]
                if i == 1:
                    continue
            else:
                lighter = smallant
                dp[i] = [dp[i - 1][0] * 2 + 1, 0]

        # 졌을땐 상관없음
        else:
            lighter = smallant
            dp[i] = [dp[i - 1][0] * 2 + 1, -1]

    print(dp)


main()
