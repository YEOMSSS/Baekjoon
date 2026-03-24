# Authored by : marigold2003
# Date : 2026-03-21
# Link : https://www.acmicpc.net/problem/34729


import sys

input = sys.stdin.readline


# [Summary] 팔정도 모니터링

# 팔정도는 길이 4개 있다. x=0, y=0, y=x, y=-x.
# 각 길에 한 사람씩 배치한다. (t,0), (0,t), (t,t), (t,-t)

# 스피커가 N(<= 10K)개가 설치되어 있다.
# 사람에서 모든 스피커까지의 맨해튼거리의 합을 거리기반비용이라 한다.
# 네 사람의 거리기반비용 G(t)의 최솟값을 구하시오.


def main() -> None:

    # [Ideas]

    # 0부터 t를 늘려가면 G(t)가 점점 줄어들다가 어느 순간 다시 늘어날 것이다.
    # 아래로 볼록한 그래프가 그려질 것...
    # 아, 이게 삼분탐색이구나!

    # 이분탐색이랑 방식이 비슷한 건 알겠는데, 목적이 완전 다르네.
    # 얘는 최대나 최소만 찾을 수 있구나.

    # y = f(x)로 찾으면, y값을 계산해 내면 된다.
    # 각 점에서 모든 스피커와의 거리를 구해서 다 더하지 뭐.

    # 아, R범위 확인을 왜 안했지? ㅋㅋㅋ... 마지막에 비교해주자.

    ##########

    N, R = map(int, input().split())
    speaker_coords = [tuple(map(int, input().split())) for _ in range(N)]

    # y값을 계산하자.
    def f(t):
        result = 0

        for sx, sy in speaker_coords:
            result += abs(sx) + abs(sy - t)
            result += abs(sx - t) + abs(sy)
            result += abs(sx - t) + abs(sy - t)
            result += abs(sx - t) + abs(sy + t)

        return result

    # int 삼분탐색 예시
    def ternary_search(low, high):
        # 둘 다 정수를 유지하기 위해 low <= m1 < m2 <= high 구조 유지
        while high - low >= 3:
            # 셋으로 나눠 m1, m2를 지정하자.
            m1 = (2 * low + high) // 3
            m2 = (low + 2 * high) // 3

            # f(m1)이 f(m2)보다 작으면 단봉은 low-m2 사이에 있다.
            if f(m1) < f(m2):
                high = m2
            # f(m1)이 f(m2)보다 크면 단봉은 m1-high 사이에 있다.
            else:
                low = m1

        # 범위 내 후보를 전부 검사해서 뱉어주자.
        return min(f(t) for t in range(low, high + 1))

    # -R <= t <= R 범위 내에서만 찾으면 된다.
    answer = ternary_search(-R, R)
    print(answer)

    ##########

    return


# [Review]

# 이야, 백번가지고 되네?
# 또 하나 새로운 걸 알았다.
# 원리는 이분탐색이랑 똑같은데, 용도가 완전 달라.
# 정수 삼분탐색이랑 실수 삼분탐색을 구분에서 써야하는구나.


if __name__ == "__main__":
    main()
