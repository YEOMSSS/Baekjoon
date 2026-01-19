import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    N_set = set()
    for _ in range(N):
        N_set.add(input().rstrip())

    result = []
    for _ in range(M):
        string = input().rstrip()
        if string in N_set:
            result.append(string)
    result.sort()

    print(len(result))
    print("\n".join(result))


main()
