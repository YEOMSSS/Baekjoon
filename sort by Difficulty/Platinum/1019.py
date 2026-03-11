
def count_digits_1_to_N(N):

    counts = [0] * 10
    
    digit = 1 # 자릿수
    while digit <= N:
        
        higher  = N // (digit * 10) # 왼쪽 덩어리
        current = (N // digit) % 10 # 현재 자리
        lower   = N % digit         # 오른쪽 덩어리

        # 1 ~ 9
        for num in range(1, 10):
            # 현재 자리가 반복된 횟수
            counts[num] += higher * digit

            # 한 바퀴 도는 경우
            if current > num:
                counts[num] += digit
            # 중간에 멈추는 경우 아래 수에 1회 추가로 더하기 (0도 가능)
            elif current == num:
                counts[num] += lower + 1

        # 0
        if higher > 0:
            # 맨 앞에 0이 있는 경우는 제외하므로 higher - 1
            counts[0] += (higher - 1) * digit
            if current > 0:
                counts[0] += digit
            elif current == 0:
                counts[0] += lower + 1

        # 한 자리 올리기
        digit *= 10

    return counts

def main():
    N = int(input().strip())
    print(*count_digits_1_to_N(N))

if __name__ == "__main__":
    main()

# 이걸 어떻게 생각해내는거지... ??????