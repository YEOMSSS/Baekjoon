# 1~46까지 만들면 len(lst)가 1035다. 조건에서 1000까지만 확인하면 된다.


def main() -> None:
    lst = [i for i in range(1, 46) for _ in range(i)]

    A, B = map(int, input().split())

    print(sum(lst[A - 1 : B]))


if __name__ == "__main__":
    main()
