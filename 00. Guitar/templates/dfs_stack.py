# stack dfs로 순회

A, B, C = map(int, input().split())
answer = set()

stack = []
visited = set()

stack.append((0, 0, C))

while stack:

    curr = stack.pop()
    if curr in visited:
        continue

    visited.add(curr)

    # a->b 이동에서 옮겨지는 물의 양은 min(a, B빈공간)이 된다.
    a, b, c = curr

    if not a:
        answer.add(c)

    # A를 B와 C에 붓기
    if a:
        stack.append((a - min(a, B - b), b + min(a, B - b), c))
        stack.append((a - min(a, C - c), b, c + min(a, C - c)))

    # B를 A와 C에 붓기
    if b:
        stack.append((a + min(b, A - a), b - min(b, A - a), c))
        stack.append((a, b - min(b, C - c), c + min(b, C - c)))

    # C를 A와 B에 붓기
    if c:
        stack.append((a + min(c, A - a), b, c - min(c, A - a)))
        stack.append((a, b + min(c, B - b), c - min(c, B - b)))
