# 풀이

```python
from typing import DefaultDict


N = int(input())

graph = DefaultDict(list)

for i in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(N)]


def dfs(s):
    # s는 시작 노드를 의미한다. 스택을 사용하여 구현
    stack = [s]
    answer = 0

    while stack:
        # stack이 빌 때까지 반복한다.
        current = stack.pop()
        if visited[current - 1] == 0:
            visited[current - 1] = 1
            answer += 1
        for i in graph[current]:
            if visited[i - 1] == 0:
                # 현재 위치한 노드를 기준으로 연결되어 있고,
                # 방문한 적이 없는 노드만 스택에 담는다.
                stack.append(i)
    return answer - 1


print(dfs(1))
```

## 접근방법

- 난이도는 낮은 그래프 문제이며, DFS로 접근하였다.
- 연결 그래프(graph)를 만들어주고, 이것을 dfs로 1부터 돌면서 진행한다.
- 이전에 방문하지 않은 노드에 방문했다고 표시와 함께 정답을 1 더하면서 정답을 구해나간다.
- stack에 담아서 사용한다.
- stack 사용 이유: 파이썬에서 리스트를 이용해서 스택 또는 큐를 구현가능한데, pop()이 pop(0)보다 시간 복잡도가 낮다. -> 리스트 사용 시, 스택이 시간 복잡도를 더 줄일 수 있다.

## 어려웠던 부분

- 어려운 부분은 없던 문제이다.

## 새로 알게 된 것

- DFS, BFS 둘 다 가능한 문제이지만, 조금이라도 시간복잡도를 줄이기 위해 stack을 사용하였다.
