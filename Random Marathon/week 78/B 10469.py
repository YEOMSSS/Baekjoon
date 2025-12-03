# col[i] = j는 체스판 i행 j열에 퀸이 놓여있다는 의미이다.
n = 8  # 8*8 체스판
col = [0] * (n + 1)


# n_queens는 퀸을 놓는 모든 경우를 찾는다.
def n_queens(i: int, col: list, target: list) -> bool:
    # 이번 조합에서 퀸이 켭치는지 확인한다.
    if promising(i, col):
        # 퀸을 n개 놓았다면 성공.
        if i == n:
            # print(col[1: n+1])
            if target == col:
                return True
        # 퀸이 겹치진 않으나 더 놔야하는 경우 다음 행의 모든 열에 하나씩 놓아본다.
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                if n_queens(i + 1, col, target):
                    return True
    return False


# col에서 겹치는 퀸이 있는지 검사한다.
def promising(i: int, col: list) -> bool:
    k = 1
    flag = True
    # 한 행에 하나의 퀸만 둔다고 가정했으니 열과 대각선을 검사하면 된다.
    # 값이 같으면 동일 열이고, 값의 차가 인덱스의 차와 같으면 동일 대각선이다.
    while k < i and flag:
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            flag = False
        k += 1
    return flag


def main() -> None:
    target_col = [0] * (n + 1)

    # 행검사는 입력받으면서 해주자.
    for i in range(1, n + 1):
        temp = input().rstrip()
        if temp.count("*") == 1:
            target_col[i] = temp.index("*") + 1
        else:
            print("invalid")
            return

    if n_queens(0, col, target_col):
        print("valid")
    else:
        print("invalid")


main()
