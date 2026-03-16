# Authored by : marigold2003
# Date : 2026-03-16
# Link : https://www.acmicpc.net/problem/31785


import sys

input = sys.stdin.readline


# [Summary] 시소 배열

# 빈 배열 A가 있고, 그에 대한 쿼리가 Q(<= 500K)개 들어온다.

# 1 x : 배열에 x를 append한다.
# 2   : 현재 배열을 반으로 갈라 합이 큰 쪽을 남긴다. 같으면 뒤를 남긴다.
#       이후 삭제된 부분의 합을 출력한다.

# 모든 쿼리를 처리하고, 남은 원소를 차례로 출력하시오.


def main() -> None:

    # [Ideas]

    # 쿼리가 500K인걸 보면 꼬라지가 누적합이다.
    # 투포인터로 인덱스 관리하면서 누적합으로 시뮬레이션하면 될 듯.

    # 근데 이게 누적합배열이 계속 만들어져야 하는건가?
    # 누적합 배열 만들어놓고 반으로 계속 갈라주면 되겠다.

    ##########

    Q = int(input())
    acc = [0]
    length = 0

    for _ in range(Q):
        command = input().rstrip()

        if command == "2":
            mid = length // 2
            left = acc[mid] - acc[0]
            right = acc[-1] - acc[mid]

            if left > right:
                acc = acc[: mid + 1]
                length = mid
                print(right)
            # 동일시 뒤를 남긴다.
            else:
                acc = acc[mid:]
                length = length - mid
                print(left)

        else:
            acc.append(acc[-1] + int(command[2:]))
            length += 1

    answer = []
    for i in range(1, length + 1):
        answer.append(acc[i] - acc[i - 1])

    print(*answer)

    ##########

    return


# [Review]

# 누적합 응용?
# 길이 세기 헷갈리네.


if __name__ == "__main__":
    main()
