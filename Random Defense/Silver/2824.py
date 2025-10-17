from math import gcd


def main():
    N = int(input())
    N_list = map(int, input().split())
    A = 1
    for num in N_list:
        A *= num
    M = int(input())
    M_list = map(int, input().split())
    B = 1
    for num in M_list:
        B *= num

    print(str(gcd(A, B))[-9:])


if __name__ == "__main__":
    main()
