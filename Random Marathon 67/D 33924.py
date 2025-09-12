
# 그냥 swap 존나 하는 문제.
# 아니면 8칸밖에 안되니까 구현을 존나 하던가

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())
S = input().rstrip()

locate = (N - 1) * 2 + M - 1

for command in S:
    match command:
        case "A":
            locate = (locate + 4) % 8
        case "B":
            locate = (11 - locate) % 8
        case "C":
            locate = (7 - locate)
        case "D":
            match locate:
                case 0:
                    locate = 1
                case 1 | 3 | 5:
                    locate += 2
                case 2 | 4 | 6:
                    locate -= 2
                case 7:
                    locate = 6

print((locate) // 2 + 1, locate % 2 + 1)
