import sys

input = sys.stdin.readline


# 아이디어는 제일 작은 것들을 정렬시켜 리스트를 만드는 것이다.
# 그리고 거기서 이분탐색으로 큰거를 찾으면 인덱스 범위가 나올듯.
# 반대로 큰것들을 정렬시키고 작은거를 찾으면 최소범위가 나올것이다.

from bisect import bisect_left, bisect_right


def main() -> None:
    N = int(input())

    # 최솟값, 최댓값 형태로 저장
    # min_to_max = []
    # for i in range(N):
    #     a, b = map(int, input().split())
    #     min_to_max.append((a - b, a + b))

    min_to_max = tuple(
        (a - b, a + b) for a, b in tuple(map(int, input().split()) for _ in range(N))
    )

    # sorted는 iterable을 받아서 list형으로 반환한다.
    min_values = sorted(x[0] for x in min_to_max)
    max_values = sorted(x[1] for x in min_to_max)

    # 입력되었던 순서대로 출력한다.
    for i in range(N):
        print(
            # 작은거 찾을 땐 동일할 때 최좌측값 뽑아야하니까 left 사용
            # 인덱스가 1부터 시작하게 출력되어야 하므로 +1
            bisect_left(max_values, min_to_max[i][0]) + 1,
            # 큰거 찾을 땐 동일할 때 최우측값 뽑아야하니까 right 사용 후 자신이 제외되니 -1
            # 인덱스가 1부터 시작하게 출력되어야 하므로 +1
            bisect_right(min_values, min_to_max[i][1]),
        )


if __name__ == "__main__":
    main()
