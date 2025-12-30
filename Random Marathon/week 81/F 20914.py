import sys

input = sys.stdin.readline

from collections import deque


# 인접 키 문자열 튜플
graph = (
    "QWSZ",
    "VGHN",
    "XDFV",
    "SERFXC",
    "WSDR",
    "DRTGVC",
    "TFYHVB",
    "YUGJBN",
    "UJKO",
    "UHIKNM",
    "IOJLM",
    "KOP",
    "NJK",
    "BHJM",
    "IKLP",
    "OL",
    "AW",
    "EDFT",
    "WAZXDE",
    "RFGY",
    "YHJI",
    "CFGB",
    "QASE",
    "ZSDC",
    "TGHU",
    "ASX",
)


def main() -> None:

    T = int(input())

    for _ in range(T):

        string = input().rstrip()

        # 첫 글자를 누른 상태
        result = 1

        # bfs용 큐 만들기
        queue = deque()

        # char단위로 포문 돌리기, 이동할 문자 기준
        for i in range(1, len(string)):

            # 방문배열 초기화
            visited = [False for _ in range(26)]

            queue.append(string[i - 1])
            visited[ord(string[i - 1]) - 65] = True

            # bfs 활용 최단거리 탐색
            while queue:

                # 레벨 구분용 포문
                for _ in range(len(queue)):
                    current = queue.popleft()

                    # break로 나가면 2가 한번 더 더해지니까 뺀 후 탈출한다.
                    if current == string[i]:
                        result -= 2
                        queue.clear()
                        break

                    # 미방문 시 큐에 push
                    for nei in graph[ord(current) - 65]:
                        if visited[ord(nei) - 65]:
                            continue

                        visited[ord(nei) - 65] = True
                        queue.append(nei)

                # 이동시 2초
                result += 2

            # 입력시 1초
            result += 1

        print(result)


main()
