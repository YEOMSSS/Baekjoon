# 하노이탑은 간단하다.
# 중간기둥에 제일 큰거 빼고 다 옮기고, 도착기둥에 제일 큰거 옮기고,
# 다시 중간기둥에 있는걸 전부 도착기둥에 옮기는 것을 반복하면 된다.


# 옮길 기둥 개수, 출발기둥, 도착기둥, 중간기둥
def hanoi(n, A, C, B) -> None:

    if n == 1:
        print(A, C)
        return

    # 목표원반이 아닌 나머지를 A->B
    hanoi(n - 1, A, B, C)
    # 목표원반 A->C
    print(A, C)
    # 옮겨뒀던 나머지 기둥 B->C
    hanoi(n - 1, B, C, A)


def main() -> None:
    N = int(input())

    print(2**N - 1)

    if N <= 20:
        hanoi(N, 1, 3, 2)


if __name__ == "__main__":
    main()
