# 제일 안자라는놈부터 잘라버리면 되는거같은데?

import sys

input = sys.stdin.readline


def main():
    N = int(input())
    trees = list(map(int, input().split()))
    tree_grows = list(map(int, input().split()))
    tree_grows_dict = {}
    for i, grow in enumerate(tree_grows):
        tree_grows_dict[i] = grow

    tree_grows_sorted = sorted(tree_grows_dict.items(), key=lambda x: x[1])

    result = 0
    for i in range(N):
        result += trees[tree_grows_sorted[i][0]]
        result += tree_grows_sorted[i][1] * i

    print(result)


main()
