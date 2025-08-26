
import sys
input = sys.stdin.readline

def main():
    ja = "aeiou"

    while True:
        arr = input().rstrip()
        if arr == "end":
            return

        length = len(arr)
        if length == 1:
            print(f"<{arr}> is acceptable.")
            continue

        for ch in ja:
            if ch in arr:
                break
        else:
            print(f"<{arr}> is not acceptable.")
            continue

        if length == 2:
            if arr == "ee" or arr == "oo" or not arr[0] == arr[1]:
                print(f"<{arr}> is acceptable.")
                continue
            else:
                print(f"<{arr}> is not acceptable.")
                continue

        # 가장 마지막 두 자리 겹침이 체크가 안되고 있었다.
        if arr[-1] == arr[-2]:
            if arr[-2 :] == "ee" or arr[-2 :] == "oo":
                pass
            else:
                print(f"<{arr}> is not acceptable.")
                continue

        for i in range(length - 2):

            if arr[i] == arr[i + 1]:
                if arr[i : i + 2] == "ee" or arr[i : i + 2] == "oo":
                    pass
                else:
                    print(f"<{arr}> is not acceptable.")
                    break

            temp = 3
            for j in range(3):
                if arr[i + j] in ja:
                    temp += 1
                else:
                    temp -= 1

            if temp == 0 or temp == 6:
                print(f"<{arr}> is not acceptable.")
                break

        else:
            print(f"<{arr}> is acceptable.")

main()



