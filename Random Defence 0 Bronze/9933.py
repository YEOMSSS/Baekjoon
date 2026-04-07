# Authored by : marigold2003
# Date : 2026-02-18
# Link : https://www.acmicpc.net/problem/9933


import sys

input = sys.stdin.readline


# [Summary] 민균이의 비밀번호

# string을 value로 갖는 arr이 들어온다.
# 이중에 딱 한 쌍만 서로 역순 관계에 있다.
# 찾아서 길이와 가운데 글자를 출력해 봐라.


def main() -> None:

    # [Ideas]

    # 입력되는 족족 뒤집어서 set에 집어넣고
    # 입력되는 족족 set에 자신이 있는지 검사

    # 팰린드롬 처리에 유의할 것.

    ##########

    N = int(input())
    string_set = set()

    for _ in range(N):
        string = input().rstrip()

        # set에 뒤집힌 자신을 집어넣기
        string_set.add(string[::-1])

        # 뒤집힌 자신이 set에 들어있는지 확인
        if string in string_set:
            length = len(string)
            print(length, string[length // 2])
            return

    ##########

    return


# [Review]

# add를 if보다 먼저 진행하면 팰린드롬도 확인 가능하다.
# 예제가 없었다면 틀렸을 듯.


if __name__ == "__main__":
    main()
