
# 삽입정렬은 인덱스1부터 확인한다.
# 일단 자신을 들어올린다.
# 왼쪽에 있는게 자신보다 크면 그놈을 자기 자리에 놓고 한칸 왼쪽으로 간다.
# 왼쪽에 더 없거나 왼쪽에 있는게 자신보다 작으면 자신을 내려놓고 중단한다.

# 얘도 O(n2)임.
# 비교까지 들어가면 무조건 시간초과 날 듯? 바뀐부분만 비교하기.

def insertion_sort(arr1, arr2, n):
    diff = 0
    for i in range(n):
        if arr1[i] != arr2[i]:
            diff += 1

    # 배열 A는 0부터 시작하므로 인덱스를 맞춰서 1..N 대신 0..N-1을 사용
    for i in range(1, n):  # 의사코드에서 2..N → 파이썬에서는 1..N-1
        locate = i - 1
        current = arr1[i]
    
        # 왼쪽으로 끝까지 가거나 자신보다 작은게 나오기 전까지 반복
        while locate >= 0 and current < arr1[locate]:

            before_diff = (arr1[locate + 1] != arr2[locate + 1])
            # 자신보다 큰 놈을 자기 자리에 놓는다.
            arr1[locate + 1] = arr1[locate]
            after_diff = (arr1[locate + 1] != arr2[locate + 1])
            diff += after_diff - before_diff

            # 문제에서 요구하는 조건 비교하기
            if diff == 0:
                return 1

            # 자신은 한 칸 왼쪽으로 간다.
            locate -= 1

        # 바로 끝난 경우가 아닐 때만 자신을 내려놓기
        if locate + 1 != i:

            before_diff = (arr1[locate + 1] != arr2[locate + 1])
            arr1[locate + 1] = current
            after_diff = (arr1[locate + 1] != arr2[locate + 1])
            diff += after_diff - before_diff

            # 문제에서 요구하는 조건 비교하기
            if diff == 0:
                return 1

    return 0

def main():
    N = int(input())
    arr_A = list(map(int, input().split()))
    arr_B = list(map(int, input().split()))

    print(insertion_sort(arr_A, arr_B, N))
    

if __name__ == "__main__":
    main()
