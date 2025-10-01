
import sys
input = sys.stdin.readline

rank = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]


def func(arr, N):
    temp = []
    for pitch in arr:
        if len(pitch) == 2:
            if pitch[1] == "b":
                index = rank.index(pitch[0]) - 1
            elif pitch[1] == "#":
                index = rank.index(pitch[0]) + 1
        else:
            index = rank.index(pitch)

        temp.append(rank[(index + N) % 12])

    return temp


def main():
    while True:
        pitches = list(input().split())
        if pitches[0] == "***":
            return
        check = int(input())

        if check < 0:
            check = check % 12 - 12
        else:
            check %= 12

        result = func(pitches, check)
        print(*result)


if __name__ == "__main__":
    main()

# 브1치곤 좀 어려운거같은데?
