import sys

input = sys.stdin.readline


# 입력이 다각형을 이루는 순서대로 들어온다. 고맙게도

# 신발끈 공식을 이용한다.
# |(x1y2, x2y3, ... xny1) - (y1x2, y2x3, ... ynx1)| / 2 를 하면 된다.


def main():
    N = int(input())

    dots = tuple(tuple(map(int, input().split())) for _ in range(N))

    result = dots[N - 1][0] * dots[0][1] - dots[N - 1][1] * dots[0][0]
    for i in range(N - 1):
        result += dots[i][0] * dots[i + 1][1] - dots[i][1] * dots[i + 1][0]

    answer = abs(result) / 2
    print(f"{answer:.1f}")


def main2():
    N = int(input())
    x, y = [], []
    for _ in range(N):
        px, py = map(int, input().split())
        x.append(px)
        y.append(py)

    # 마지막 점과 첫 점을 연결하기 위해 첫 좌표를 추가
    x.append(x[0])
    y.append(y[0])

    sum1 = sum(x[i] * y[i + 1] for i in range(N))
    sum2 = sum(y[i] * x[i + 1] for i in range(N))

    print(f"{abs(sum1 - sum2) / 2:.1f}")


if __name__ == "__main__":
    main2()
