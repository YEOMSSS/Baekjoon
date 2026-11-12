# 중위 순회 inorder

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/04-20 - 620. 트리 1 250705 ~ 250707]]

원문 사본: [[Obsidian/원본 - Python README]]

순서: 왼쪽 → 루트 → 오른쪽

    def inorder(node):
        if node:
            inorder(node.left)        # 1. 왼쪽 서브트리 순회
            print(node.value)         # 2. 루트 처리
            inorder(node.right)       # 3. 오른쪽 서브트리 순회

이진 탐색 트리(BST)의 경우, 중위 순회를 하면 오름차순 정렬된 결과가 나옴.

## 보충 설명과 예시

이진 탐색 트리에서는 중위 순회 결과가 오름차순이다.
```python
def inorder(node):
    if node:
        inorder(node.left); print(node.value); inorder(node.right)
```
