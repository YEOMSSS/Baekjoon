# 시뮬레이션.


def main() -> None:
    N = int(input())

    clap_count = 0
    for num in range(1, N + 1):
        s_num = str(num)
        clap_count += s_num.count("3") + s_num.count("6") + s_num.count("9")

    print(clap_count)


if __name__ == "__main__":
    main()
