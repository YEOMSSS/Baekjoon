import sys

input = sys.stdin.readline


def main():
    # 과목 수, 주어진 마일리지
    N, M = map(int, input().split())

    need_Ms = []
    for _ in range(N):
        # 신청자 수, 수강 가능 인원
        p, l = map(int, input().split())
        applicants = sorted(list(map(int, input().split())), reverse=True)

        if l <= p:
            need_Ms.append(applicants[l - 1])
        else:  # 신청자가 수강인원보다 적으면 1로도 수강가능
            need_Ms.append(1)

    total = 0
    for i, m in enumerate(sorted(need_Ms)):
        total += m
        if total > M:
            print(i)
            return

    print(N)


if __name__ == "__main__":
    main()
