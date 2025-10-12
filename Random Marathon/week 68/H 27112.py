
import sys
input = sys.stdin.readline

# 그리디로 풀 수 있나.
# 그냥 다 더하면 안되나? 평일인 일수 구해서 빼준 나머지가 초과근무지.
# 음, 마감일이라는 게 있구나. 급한거 우선으로 정렬하자.

def main():

    N = int(input())

    works = [list(map(int, input().split())) for _ in range(N)]
    # 일단 급한 일부터 정렬해보자.
    works.sort(key= lambda x: x[0])

    # 평일에는 2회 일할 수 있고, 주말에는 1회만 일할 수 있다.
    # 근데 최대한 초과근무는 적게 해야하는데..

    day = 0           # 시뮬레이션한 마지막 날짜(0일부터 시작)
    normal = 0        # 평시 근무로 확보한 총 작업칸(평일에만 +1)
    overtime = 0      # 시간 외 근무로 확보한 총 작업칸(매일 +1)
    answer = 0        # 실제로 사용한 시간 외 근무 횟수

    for d, t in works:
        # 현재 작업의 마감일 d까지 달력을 늘려가며 잔여 칸 확보하기.
        # 사용가능한 날만큼 계속 더해주는 느낌.
        while day < d:
            # 01234는 평일, 56은 주말.
            # 평일에만 평시근무 사용가능 횟수가 늘어난다.
            if day % 7 < 5:
                normal += 1
            # 초과근무는 매일 할 수 있다.
            overtime += 1
            day += 1

        # 이 작업 t칸을 먼저 평시에서 소비
        if normal >= t:
            normal -= t
        # 평시근무로 다 못하면 초과 뛰어야지
        else:
            need = t - normal
            normal = 0
            if overtime >= need:
                # 초과근무에서 소비해주고, 소비한만큼 정답에 쌓아주기.
                overtime -= need
                answer += need
            # 초과근무로도 다 못채우면 종료
            else:
                print(-1)
                return

    print(answer)

if __name__ == "__main__":
    main()

# 쉬운 문제는 아니었다. 구현 방법을 발상하는게 좀 어려웠네

