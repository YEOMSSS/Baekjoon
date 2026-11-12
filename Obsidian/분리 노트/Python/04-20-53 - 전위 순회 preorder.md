# 전위 순회 preorder

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/04-20 - 620. 트리 1 250705 ~ 250707]]

원문 사본: [[Obsidian/원본 - Python README]]

순서: 루트 → 왼쪽 → 오른쪽

    def preorder(node):
        if node:
            print(node.value)         # 1. 루트 처리
            preorder(node.left)       # 2. 왼쪽 서브트리 순회
            preorder(node.right)      # 3. 오른쪽 서브트리 순회

## 보충 설명과 예시

전위 순회는 루트→왼쪽→오른쪽 순서다.
```python
def preorder(node):
    if node:
        print(node.value)
        preorder(node.left); preorder(node.right)
```
