# 전부 꽉 차 있을 경우 최대 5050번 확인하면 된다.
# 5칸까지 비어있으니까, 5! = 120.
# 120*5050 < 200*5000 = 1000000번정도면 브루트포스로.

from itertools import permutations


def main():

    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    erased = [0 for _ in range(N + 1)]
    e_idx = []
    for i in range(N):
        temp = arr[i]
        if not temp:
            e_idx.append(i)
        else:
            erased[arr[i]] = 1

    e_num = []
    for i in range(1, N + 1):
        if not erased[i]:
            e_num.append(i)

    erased = permutations(e_num, len(e_num))

    result = 0
    for e_perm in erased:
        check = 0

        for i in range(len(e_num)):
            arr[e_idx[i]] = e_perm[i]

        for i in range(N):
            for j in range(i + 1, N):
                if arr[i] < arr[j]:
                    check += 1

        if check == S:
            result += 1

    print(result)


main()
