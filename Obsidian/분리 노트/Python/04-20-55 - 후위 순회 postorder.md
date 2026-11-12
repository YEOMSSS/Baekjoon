# 후위 순회 postorder

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/04-20 - 620. 트리 1 250705 ~ 250707]]

원문 사본: [[Obsidian/원본 - Python README]]

순서: 왼쪽 → 오른쪽 → 루트

    def postorder(node):
        if node:
            postorder(node.left)      # 1. 왼쪽 서브트리 순회
            postorder(node.right)     # 2. 오른쪽 서브트리 순회
            print(node.value)         # 3. 루트 처리

## 보충 설명과 예시

후위 순회는 자식을 먼저 처리해야 할 때 쓴다.
```python
def postorder(node):
    if node:
        postorder(node.left); postorder(node.right); print(node.value)
```
