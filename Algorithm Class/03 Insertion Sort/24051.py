# 삽입정렬은 인덱스1부터 확인한다.
# 일단 자신을 들어올린다.
# 왼쪽에 있는게 자신보다 크면 그놈을 자기 자리에 놓고 한칸 왼쪽으로 간다.
# 왼쪽에 더 없거나 왼쪽에 있는게 자신보다 작으면 자신을 내려놓고 중단한다.

# 얘도 O(n2)임.


def insertion_sort(arr, n, k):
    cnt = 0
    # 배열 A는 0부터 시작하므로 인덱스를 맞춰서 1..N 대신 0..N-1을 사용
    for i in range(1, n):  # 의사코드에서 2..N → 파이썬에서는 1..N-1
        locate = i - 1
        current = arr[i]

        # 왼쪽으로 끝까지 가거나 자신보다 작은게 나오기 전까지 반복
        while locate >= 0 and current < arr[locate]:
            # 자신보다 큰 놈을 자기 자리에 놓는다.
            arr[locate + 1] = arr[locate]

            # 문제에서 요구하는 조건 k 맞추기
            cnt += 1
            if cnt == k:
                return arr[locate + 1]

            # 자신은 한 칸 왼쪽으로 간다.
            locate -= 1

        # 바로 끝난 경우가 아닐 때만 자신을 내려놓기
        if locate + 1 != i:
            arr[locate + 1] = current

            # 문제에서 요구하는 조건 k 맞추기
            cnt += 1
            if cnt == k:
                return arr[locate + 1]

    return -1


def main():
    N, K = map(int, input().split())
    arr_input = list(map(int, input().split()))

    print(insertion_sort(arr_input, N, K))


if __name__ == "__main__":
    main()
