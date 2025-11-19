import sys

input = sys.stdin.readline


def func(string):
    return [string.count("L"), string.count("O"), string.count("V"), string.count("E")]


def main():
    name_score = func(input().rstrip())

    result = 0
    result_team = []
    N = int(input())
    for i in range(N):
        team = input().rstrip()
        team_score = func(team)

        final_score = [name_score[i] + team_score[i] for i in range(4)]

        score = 1
        for i in range(3):
            for j in range(i + 1, 4):
                score *= final_score[i] + final_score[j]

        score %= 100
        if result < score:
            result = score
            result_team = [team]
        elif result == score:
            result_team.append(team)
    result_team.sort()
    print(result_team[0])


main()
