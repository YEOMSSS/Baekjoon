
import sys
input = sys.stdin.readline

def main():

    N = int(input())
    arr = [input().rstrip() for _ in range(N)][::-1]
    K = int(input())
    arr_K = set([input().rstrip() for _ in range(K)])

    rank = [] # 여기에 순서대로 저장됨
    rank_set = set()

    for string in arr:
        if string in rank_set:
            continue
        if string in arr_K:
            print(string)
        else:
            rank.append(string)
        rank_set.add(string)

    for string in rank:
        print(string)


if __name__ == "__main__":
    main()

# 한번만 돌아도 될걸 두번 돌아서 시간초과났네, 염병
