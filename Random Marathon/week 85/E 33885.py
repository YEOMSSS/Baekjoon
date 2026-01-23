import sys

input = sys.stdin.readline

from itertools import combinations


def main() -> None:
    N, M = map(int, input().split())
    schedules = [list(input().split()) for _ in range(N)]

    # 1~N개 조합뽑기
    for n in range(1, N + 1):
        # n개 조합 확인
        for comb in combinations(range(N), n):

            curr_score = 0
            curr_timetable = set()

            # 중복체크 플래그
            flag = False

            # 이번 조합이 되는지 확인
            for i in comb:
                # 학점, 요일 수
                c, s = map(int, schedules[i][:2])

                # 시간표 확인
                for j in range(s):
                    # 요일 + 시간으로 시간표 운영
                    time = schedules[i][2 + j * 2] + schedules[i][3 + j * 2]

                    # 겹치면 불가능
                    if time in curr_timetable:
                        flag = True
                        break
                    curr_timetable.add(time)

                # 중복시 스케줄 실행 불가
                if flag:
                    break

                curr_score += c

            # 학점 만족시 종료
            if curr_score >= M:
                print("YES")
                return

    print("NO")


if __name__ == "__main__":
    main()
