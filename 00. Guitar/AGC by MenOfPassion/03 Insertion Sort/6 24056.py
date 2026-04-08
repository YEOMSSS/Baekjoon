import sys

input = sys.stdin.readline


# 초반에 오름차순으로 쭉 있고, 오름차순이 터지는 순간부터는 오리지널이랑 같아야한다.


def func(arr1, arr2, N):

    # 정렬된 배열이 들어온 경우 arr2는 arr1이어야만 한다.
    if arr1 == sorted(arr1):
        if arr1 == arr2:
            return 1
        else:
            return 0

    # 교집합의 크기는 N아니면 N-1이어야만 한다.
    intersection_size = len(set(arr1) & set(arr2))
    if not (intersection_size == N or intersection_size == N - 1):
        return 0

    # 오름차순이 끊긴 이후 arr2는 arr1과 같아야 한다.
    prev = arr2[0]
    for i, cur in enumerate(arr2[1:]):
        if cur >= prev:
            prev = cur
        else:
            break

    if arr1[i + 2 :] == arr2[i + 2 :]:
        return 1
    else:
        return 0


def main():
    N = int(input())
    arr_A = list(map(int, input().split()))
    arr_B = list(map(int, input().split()))
    print(func(arr_A, arr_B, N))


if __name__ == "__main__":
    main()
