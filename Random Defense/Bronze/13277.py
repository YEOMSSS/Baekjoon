# #include <stdio.h>

# int main(void)
# {
#     int N, M;
#     scanf("%d %d", &N, &M);

#     printf("%d", N * M);
#     return 0;
# }


import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    print(N * M)


main()
