from collections import deque


buf = deque()


def main():

    N = int(input())

    current = 0
    while True:
        data = int(input())

        if data == -1:
            return

        # 버퍼가 비어있으면 0이 안들어온다는 조건
        if data == 0:  # and buf
            buf.popleft()
            current -= 1
            continue

        if current >= N:
            continue

        buf.append(data)
        current += 1


main()

if buf:
    print(*buf)
else:
    print("empty")
