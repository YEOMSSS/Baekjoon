sticks = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def main() -> None:
    N = int(input())
    for i in range(100):
        cur = sticks[i % 10] + sticks[i // 10]
        for j in range(100):
            if i + j >= 100:
                break
            if (
                cur
                + sticks[j % 10]
                + sticks[j // 10]
                + sticks[(i + j) % 10]
                + sticks[(i + j) // 10]
                + 4
                == N
            ):
                print(f"{i:02}+{j:02}={i+j:02}")
                return

    print("impossible")


main()
