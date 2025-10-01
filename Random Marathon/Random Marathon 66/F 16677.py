
import sys
input = sys.stdin.readline

def main():
    word_m = input().rstrip()
    len_m = len(word_m)
    N = int(input())

    gapBunSsa = float("-inf")
    answer = ""
    for _ in range(N):
        w, g = input().split()
        g = int(g)

        current_index = 0
        for char in w:
            if char == word_m[current_index]:
                current_index += 1

            # 만들 수 있는 단어인지 확인 후
            if current_index == len_m:
                # 갑분싸 가성비가 더 좋으면 갱신
                gapBunSsa_w = g / (len(w) - len_m)
                if gapBunSsa < gapBunSsa_w:
                    answer = w
                    gapBunSsa = gapBunSsa_w
                break

    if answer == "":
        print("No Jam")
        return
    else:
        print(answer)
        return

if __name__ == "__main__":
    main()