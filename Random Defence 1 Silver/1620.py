# Authored by : marigold2003
# Date : 2026-11-25
# Link : https://www.acmicpc.net/problem/1620


import sys

input = sys.stdin.readline


# [Summary] 나는야 포켓몬 마스터 이다솜

# 포켓몬 도감 정보를 잘 입력해서 저장하고,
# 번호가 들어오면 이름을, 이름이 들어오면 번호를 출력하자.


def main() -> None:

    # [Ideas]

    # 딕셔너리를 두 개 만들자. 이름-번호, 번호-이름.
    # 단일로 해도 상관없긴 하겠는데? 겹칠일이 없으니
    # 근데 str 비용이 더 드는거 같기도 하고.

    ##########

    N, M = map(int, input().split())

    id_to_name = dict()
    name_to_id = dict()

    for id in range(1, N + 1):
        name = input().rstrip()
        id_to_name[id] = name
        name_to_id[name] = id

    for _ in range(M):
        query = input().rstrip()
        if query.isdigit():
            print(id_to_name[int(query)])
        else:
            print(name_to_id[query])

    ##########

    return


# [Review]

# 이런 스타일의 번외문제가 있었던 듯한 기억.
# 아, 그래. 9987번


if __name__ == "__main__":
    main()
