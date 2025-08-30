
import sys
input = sys.stdin.readline

def Checker():
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    square_sets = [set() for _ in range(9)]

    for i in range(9):

        # row 확인
        if len(set(sudoku[i])) != 9:
            return False
        
        # col 확인
        col = [
            sudoku[0][i], sudoku[1][i], sudoku[2][i],
            sudoku[3][i], sudoku[4][i], sudoku[5][i],
            sudoku[6][i], sudoku[7][i], sudoku[8][i]
        ]
        if len(set(col)) != 9:
            return False
        
        # square 확인용 set 채우기
        for j in range(9):
            square_sets[(i // 3) * 3 + (j // 3)].add(sudoku[i][j])

    # square 확인
    for square in square_sets:
        if len(square) != 9:
            return False

    return True

def main():
    N = int(input())

    for i in range(N):
        if Checker():
            print(f"Case {i + 1}: CORRECT")
        else:
            print(f"Case {i + 1}: INCORRECT")
        
        if i == N - 1:
            return

        # 공백 무시용
        temp = input()

if __name__ == "__main__":
    main()