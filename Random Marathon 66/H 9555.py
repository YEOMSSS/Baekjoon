
directions = [
    (-1, -1), (-1, 0), (-1, 1), (0, -1),
    (0, 1), (1, -1), (1, 0), (1, 1)
]

def func():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 인접이 확인된 학교 저장용
    used_set = set()

    # arr의 모든 칸 확인
    for y in range(N):
        for x in range(M):

            current = arr[y][x]
            # 이미 확인한 학교는 패스
            if current in used_set:
                continue
            # -1은 빈칸이니까 패스
            if current == -1:
                continue

            # 8방향에 대하여 전부 확인
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                # 인덱스 확인
                if ny < 0 or N <= ny or nx < 0 or M <= nx:
                    continue
                # 인접이 확인되면 set에 추가
                if current == arr[ny][nx]:
                    used_set.add(current)

    # 인접한 학교의 수
    print(len(used_set))
    return



def main():
    T = int(input())

    for _ in range(T):
        func()

    return

if __name__ == "__main__":
    main()