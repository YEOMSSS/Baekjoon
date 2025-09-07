
# 팀 구성원의 수에 자신을 포함시키는 것을 잊으면 안 된다.

import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    a, b, c = map(int, input().split())
    total = a + b + c
    
    arr_dict = {}
    for i in range(1, N + 1):
        arr_dict[i] = sum(map(int, input().split()))

    sorted_arr = sorted(arr_dict.items(), key= lambda x: x[1], reverse= True)

    result = [0]
    cnt = 1
    for candidate in sorted_arr:
        if cnt == M:
            break
        if candidate[1] <= total:
            result.append(candidate[0])
            cnt += 1

    print(*result)


if __name__ == "__main__":
    main()