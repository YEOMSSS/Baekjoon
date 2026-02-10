import sys

input = sys.stdin.readline


def main() -> None:
    N1, N2 = map(int, input().split())
    ants = list(input().rstrip())[::-1]
    ant_set = set(ants)  # 오른쪽으로 가야하는 애들만 저장
    ants += list(input().rstrip())
    T = int(input())

    length = len(ants)

    flag = False

    for _ in range(T):
        flag = False
        for i in range(length - 1):

            # 전차례에 변경되었으면 한번 건너뛰기
            if flag:
                flag = False
                continue
            # 왼쪽으로 가는애들은 먼저 올 일이 없다.
            if ants[i] not in ant_set:
                continue
            # 오른쪽으로 가는애들이 뒤에 올 일이 없다.
            if ants[i + 1] in ant_set:
                continue
            ants[i], ants[i + 1] = ants[i + 1], ants[i]
            flag = True

    print("".join(ants))


main()
