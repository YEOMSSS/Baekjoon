# x는 질량의 비율, 총질량 100이라 하고 그냥 질량으로 사용

# 밀도d = 질량 / 부피
# 질량 = 밀도d * 부피
# 부피 = 밀도d / 질량


def main() -> None:
    d1, d2, x = map(int, input().split())

    answer = 100 / (x / max(d1, d2) + (100 - x) / min(d1, d2))
    print(answer)


if __name__ == "__main__":
    main()
