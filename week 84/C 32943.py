import sys

input = sys.stdin.readline


def main() -> None:

    # 학생수, 좌석수, 로그수
    X, C, K = map(int, input().split())
    log = list(tuple(map(int, input().split())) for _ in range(K))

    # 신청시각순으로 오름차순 정렬
    log.sort(key=lambda x: x[0])

    students = {}
    seats = [0] * (C + 1)

    # 신청시각, 좌석번호, 학번
    for t, s, n in log:

        # 이미 주인이 있는 좌석이면 패스
        if seats[s]:
            continue

        seats[s] = n

        current = students.get(n)
        # 자리가 이미 있던 학생이면 이전 자리는 비우기
        if students.get(n):
            seats[current] = 0

        # 앉은 자리 갱신하기
        students[n] = s

    for n, s in sorted(students.items()):
        print(n, s)


if __name__ == "__main__":
    main()
