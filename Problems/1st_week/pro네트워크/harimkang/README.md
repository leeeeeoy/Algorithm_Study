# 풀이

```python
def solution(n, computers):

    # dfs방식으로, 노드를 하나씩 방문하면서 방문 여부를 체크하는 함수
    def dfs(s):
        # s는 시작 노드를 의미한다. 스택을 사용하여 구현
        stack = [s]

        while stack:
            # stack이 빌 때까지 반복한다.
            current = stack.pop()
            if visited[current] == 0:
                visited[current] = 1
            for i in range(n):
                if visited[i] == 0 and computers[current][i] == 1:
                    # 현재 위치한 노드를 기준으로 연결되어 있고,
                    # 방문한 적이 없는 노드만 스택에 담는다.
                    stack.append(i)

    answer = 0
    # visited: 각 컴퓨터(노드)들이 연결된 상태를 확인하는 리스트
    visited = [0] * n

    i = 0
    # 아직 거치지 않은 노드가 있거나 index를 넘어서면 탐색 종료
    while (0 in visited) or i < n:
        if visited[i] == 0:
            dfs(i)
            answer += 1

        i += 1

    return answer
```

## 접근방법

- DFS 구현 -> stack을 이용한 반복
- visited list를 이용한 방문 체크
- 방문하지 않은 노드를 발견시, dfs 탐색 시작 및 answer + 1
- visit하지 않고, 현재 노드와 연결된 노드를 스택에 담는다.

## 어려웠던 부분

- dfs 기초적인 문제 -> 더 빠른 시간내에 풀이 가능하면 좋을 것 같다.

## 새로 알게 된 것

- 기본적인 dfs 문제 유형
