import sys

input = sys.stdin.readline

from itertools import combinations


# 결과값을 사전순 정렬해야하니 일단 다 해봐야겠다.
# 중복이 생길 가능성도 있으니 편하게 set으로 털어버리자.
# 왜 combs 안에서 정렬하려고 했을까? 단순하게 생각해야 할 때도 있는 거였다.
def main() -> None:
    string = list(input().rstrip())

    cnt = string.count("(")
    combs = (combinations(range(1, cnt + 1), i) for i in range(1, cnt + 1))

    result = set()
    for comb in combs:
        for cb in comb:
            stack = []
            buf = []
            cur = 0
            for ch in string:
                match ch:
                    case "(":
                        cur += 1
                        stack.append(cur)
                        if cur in cb:
                            continue
                        buf.append(ch)
                    case ")":
                        if stack.pop() in cb:
                            continue
                        buf.append(ch)
                    case _:
                        buf.append(ch)
            result.add(tuple(buf))

    for r in sorted(result):
        print("".join(r))


main()
