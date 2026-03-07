# Authored by : marigold2003
# Date : 2026-03-07
# Link : https://www.acmicpc.net/problem/1592


import sys

input = sys.stdin.readline


# [Summary] 영식이와 친구들

# 친구들이 원형으로 모여 시계방향으로 1~N(<=50)이 적힌 자리에 앉는다.
# 1번이 공을 받아서 다른 사람에게 공을 던지는 것을 반복하고
# 한 사람이 공을 M번 받으면 게임은 끝난다.

# 공을 M번보다 적게 받은 사람이 공을 던질 때
# 현재 공을 받은 횟수가 홀수번이면 시계방향 L번째에게,
# 짝수번이면 반시계방향 L번째에게 공을 던진다.

# 공을 총 몇 번 던지는지 구하시오.


def main() -> None:

    # [Ideas]

    # 시뮬레이션이잖아?
    # 이정도는 rotate 안쓰고 그냥 list로 처리하자.

    ##########

    N, M, L = map(int, input().split())

    counts = [0] * N
    counts[0] += 1
    curr = 0

    answer = 0

    if M == 1:
        print(answer)
        return

    while True:

        # 홀수면 시계방향 L번째에게 패스
        if counts[curr] // 2:
            answer += 1
            curr = (curr + L) % N
            counts[curr] += 1
        else:
            answer += 1
            curr = (curr - L) % N
            counts[curr] += 1

        if counts[curr] == M:
            break

    print(answer)

    ##########

    return


# [Review]

# 예제 없었으면 정답비율 30%까지 본다


if __name__ == "__main__":
    main()
