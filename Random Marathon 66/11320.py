
# A와 B가 주어진다. A는 B로 나누어떨어진다.
# 길이가 A인 정삼각형을 B인 정삼각형으로 덮는다. 몇 개 필요한가?
# A // B의 제곱이 될 듯.
# 왜 그런진 모르겠네, 존나 신기하네,,,

def function(A, B):
    result = (A // B) ** 2
    print(result)

    return

def main():
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        function(A, B)

    return

if __name__ == "__main__":
    main()

