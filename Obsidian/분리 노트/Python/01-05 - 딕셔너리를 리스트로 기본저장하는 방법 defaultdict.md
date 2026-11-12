# 딕셔너리를 리스트로 기본저장하는 방법 defaultdict

---
tags: [baekjoon, python, algorithm]
---

⬆ 상위 노트: [[Obsidian/분리 노트/Python/01 - 00. 기타]]

원문 사본: [[Obsidian/원본 - Python README]]

```python
for i, char in enumerate(text):
    # 각 문자(키)가 딕셔너리에 없으면 빈 리스트를 만들고 인덱스 추가
    char_indices.setdefault(char, []).append(i)
```

또는

```python
from collections import defaultdict

# 모든 value는 기본적으로 리스트(list)임을 선언
char_indices = defaultdict(list)
```

defaultdict는 접근만 해도 새 key가 생기기 때문에  
웬만하면 get으로 value를 받아오는 편이 좋다.
