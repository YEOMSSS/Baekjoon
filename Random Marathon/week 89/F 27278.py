# Authored by : marigold2003
# Date : 2026-02-16
# Link : https://www.acmicpc.net/problem/27278


import sys

input = sys.stdin.readline


# [Summary] 영내순환버스

# 영내를 순환하는 버스가 있다. 버스에는 병사가 무한히 탈 수 있다.
# 지점은 N개가 있으며, 각각의 이동시간이 주어진다.
# M명의 병사를 내려주면 일과는 종료된다.

# 일과 종료 시각을 구하시오.


def main() -> None:

    # [Ideas]

    # 시뮬레이션까진 아닌것같고.
    # 어차피 버스가 무한하니까, 각 병사에 대해 따로따로 계산해도 될 듯.

    # 각 병사의 하차 시각을 구해서 제일 큰 게 답이 되겠다.

    ##########

    N, M = map(int, input().split())
    times = [0] + list(map(int, input().split()))

    # 누적합으로 바꿔서 저장하기
    # 각 칸에 시작지점 ~ 현재 지점까지 걸리는 시간이 저장된다.
    # 마지막칸은 한바퀴 도는데 걸리는 시간
    for i in range(1, N + 1):
        times[i] += times[i - 1]

    # 한 바퀴 도는 데 걸리는 시간은 상수로 해두자.
    T = times[N]

    answer = 0
    for _ in range(M):
        # 승차지점, 하차지점, 대기시작시각
        p, r, c = map(int, input().split())

        # 기본적으로 시작지점에서 현재지점까지 오는 만큼은 기다려야 함
        curr = c // T * T + times[p - 1]

        # 대기시작시각을 전체거리로 나눈 나머지를 확인한다.
        # 시작지점에서 현재지점까지 오는 시간과 어긋나면 한바퀴 더 기다려야 함
        if c % T > times[p - 1]:
            curr += T

        # 이제 이동시간을 더하면 된다.

        # N->1 의 경로를 거치지 않는 경우, r-p
        if p < r:
            curr += times[r - 1] - times[p - 1]
        # N->1 의 경로를 거치는 경우 T-p + r
        else:
            curr += (T - times[p - 1]) + times[r - 1]

        answer = max(answer, curr)

    print(answer)

    ##########

    return


# [Review]

# 이런문제는 손으로 그리면서 푸는게 빠르다.
# 헷갈리기 싫으면 노트와 펜을 꺼내오도록


if __name__ == "__main__":
    main()
