# Authored by : marigold2003
# Date : 2026-03-03
# Link : https://www.acmicpc.net/problem/25420


import sys

input = sys.stdin.readline


# [Summary] 끝까지 외친 정수의 개수

# 두 학생이 게임을 한다. 첫 1~N(100K) 사이의 정수로 진행된다.
# 이전학생이 외친 정수가 a면 현재 학생은 a+1~a+k의 정수 중 하나를 외쳐야 한다.
# 외칠 수 없는 정수 목록이 주어진다.

# 맨 처음 학생은 1~k중에서 외쳐야 한다.
# 마지막에 정수를 못 외치는 학생이 게임을 진다.

# 현재 학생이 이길 수 있는 정수가 있으면
# 이기면서 두 명의 학생이 앞으로 외칠 정수 개수의 합이 최소가 되도록 플레이하고
# 현재 학생이 이길 수 있는 정수가 없으면
# 두 명의 학생이 앞으로 외칠 정수 개수의 합이 최대가 되도록 플레이한다.

# 두 명의 학생이 외친 정수 개수의 합을 출력하시오.


def main() -> None:

    # [Ideas]

    # 시작하자마자 N 외치면 끝나니까 k로 시작제한을 뒀을 것.
    # 뭐지 그리디인가? 최소 최대니까...

    # 근데 이길 수 있는 정수가 뭐냐?
    # 일단 이해를 해보자, 이길 수 있으면 외칠 게 최소가 되도록
    # -> 이거, 막타각을 재라는 뜻인거 같은데.
    # 막타각이 나오면 죽이고, 안나오면 길게 보라는 느낌인가.

    # 일단 이 게임은 거꾸로 가는 건 불가능하다.
    # 그렇다는 건, 막타각이 안나오면 무조건 +1을 불러야 되는 거지.

    # 막타각은 어떻게 볼 수 있는가?
    # 이번 범위에 N이 포함되면 불러버리면 된다.
    # 변수는 금지목록이다. 금지목록 때문에 막타각이 더 다양하진다.
    # 현재 부른 a부터 해서 a+1~a+k가 모두 금지목록에 들어있으면 불러야 한다.
    # 이걸 다 일일이 확인할 수 있나?

    # 아니야, 그리디가 아닌 것 같아. 이길 수 있는 정수가 뭘까.
    # 게임의 전체를 판단해야 한다.

    # 좀 더 생각해보자. N을 부르는 건 중요하지 않다.
    # 결국 핵심은 a+1~a+k 중 금지되지 않은 수가 있는지 판단하는 것.

    # dp를 사용해서, dp[a]를 정의하자.
    # 직전 숫자가 a이며, 내 차례일 때 이길 수 있으면 True, 없으면 False.
    # 그렇게 해두고 게임을 진행하면, 내 범위에 False가 보이면 그걸 골라 상대를 지게 하면 된다.
    # 범위에 False가 하나만 있어도 True를 반환하게 되겠지.

    # 처음에 False가 확정된건 dp[N]밖에 없잖아.
    # 그러면 거꾸로 돌려야겠네.

    ##########

    N, K = map(int, input().split())
    banned_nums = set(map(int, input().split()))

    dp_win = [False] * (N + 1)
    # 승리까지 필요한 정수 개수
    dp_len = [0] * (N + 1)

    for a in range(N, -1, -1):
        candidates = []

        # 범위가 N까지임을 기억할 것, 외칠 수 있는 a 찾기
        for nxt in range(a + 1, min(N, a + K) + 1):
            # 금지목록에 있으면 외칠 수 없다.
            if nxt in banned_nums:
                continue
            candidates.append(nxt)

        # 외칠 수 있는 nxt가 하나도 없으면 탈락.
        if not candidates:
            dp_win[a] = False
            dp_len[a] = 0
            continue

        # a+1~a+k에서 외칠 수 있는 nxt 중에 False가 있다면 승리 가능
        win_moves = [nxt for nxt in candidates if not dp_win[nxt]]

        # 이길 수 있는 정수가 있다면, 앞으로 외칠 정수 개수의 합이 최소가 되도록 플레이
        # 그러면 승리까지 가기 위해 불러야 하는 정수 개수가 적은 nxt를 선택한다.
        if win_moves:
            dp_win[a] = True
            dp_len[a] = 1 + min(dp_len[nxt] for nxt in win_moves)
        # dp[nxt]가 전부 False여서 a로 이기는 게 불가능하다.
        # 이길 수 있는 정수가 없다면, 앞으로 외칠 정수 개수의 합이 최대가 되도록 플레이
        else:
            dp_win[a] = False
            dp_len[a] = 1 + max(dp_len[nxt] for nxt in candidates)

    # 0은 시작이다. 1~1+k범위를 검사하게 된다.
    # dp[0]은 이 게임 전체를 진행한 결과가 들어가게 된다.
    print(dp_len[0])

    ##########

    return


# [Review]

# 존나 어려운데요?
# 이런 류 처음 접하면 문제 이해도 제대로 못할듯.


if __name__ == "__main__":
    main()
