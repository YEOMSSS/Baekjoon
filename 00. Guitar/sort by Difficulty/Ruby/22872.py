import sys

sys.setrecursionlimit(10**7)

moves = []  # (a, b) 쌍을 여기다 쌓음


def move(s, e):
    """s 번 바구니 -> e 번 바구니 한 번 이동 기록"""
    moves.append((s, e))


def hanoi(n, s, m, e, state=-1):
    """
    n: 옮길 '공 블록' 개수 (하노이의 디스크 개수 느낌)
    s: 시작 바구니 번호 (1~3)
    m: 보조 바구니 번호
    e: 도착 바구니 번호
    state: 각 바구니의 '방향 상태'를 비트로 가진 값
    -1 일 때는 처음 호출용 특수 처리
    """
    # 최초 호출: state 미정(-1)일 때, 초기 상태 세팅
    if state == -1:
        if n <= 0:
            return
        # 1) 위쪽 n-1개를 1->2 로 옮기는데,
        #    "1번 기둥의 방향" 정보를 state에 1<<1 로 기록
        hanoi(n - 1, s, e, m, 1 << s)

        # 2) 가운데 공(또는 가장 아래 역할)을 1->3 으로 이동
        move(s, e)

        # 3) 나머지 n-1개를 2->3 으로 옮기는데,
        #    "3번 기둥의 방향" 정보를 state에 1<<3 로 기록
        hanoi(n - 1, m, s, e, 1 << e)
        return

    # 여기부터는 state가 정해진 상태에서의 일반 재귀

    if n <= 0:
        return

    if n == 1:
        move(s, e)
        return

    # s, e 기둥의 방향 상태가 다른 경우
    if ((state >> s) & 1) ^ ((state >> e) & 1):
        # 위쪽 n-2 개를 s -> m 로 이동
        hanoi(n - 2, s, e, m, state)
        # 가운데 두 개(실제로는 가운데 공의 양쪽 '조각')를 s -> e 로 두 번 이동
        move(s, e)
        move(s, e)
        # 나머지 n-2 개를 m -> e 로 이동
        hanoi(n - 2, m, s, e, state)

    # s, e 기둥의 방향 상태가 같은 경우
    else:
        # n == 2 인 특수 케이스
        if n == 2:
            # s -> m, s -> e, m -> e
            move(s, m)
            move(s, e)
            move(m, e)
            return

        # 1) 위쪽 n-2 개를 s -> m 로
        hanoi(n - 2, s, m, e, state)

        # 2) 가운데 두 조각을 s -> m 로 두 번
        move(s, m)
        move(s, m)

        # 3) n-2 개를 e -> m 로
        hanoi(n - 2, e, m, s, state)

        # 4) 가운데 두 조각을 m -> e 로 두 번
        move(m, e)
        move(m, e)

        # 5) 다시 n-2 개를 s -> m 로
        hanoi(n - 2, s, m, e, state)


def main():
    input = sys.stdin.readline
    N = int(input().strip())

    hanoi(N, 1, 2, 3)

    print(len(moves))
    for move in moves:
        print(*move)


if __name__ == "__main__":
    main()
