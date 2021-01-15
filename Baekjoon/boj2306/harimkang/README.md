# 풀이

```python
dna = input()
dp = [[0 for _ in dna] for _ in dna]

for i in range(1, len(dna)):
    for s in range(len(dna) - i):

        # i는 확인하려는 문자의 수
        # s는 현재 문자의 시작 위치, e는 문자의 끝
        e = s + i
        if (dna[s] == "a" and dna[e] == "t") or (dna[s] == "g" and dna[e] == "c"):
            # 현재 확인 문자의 양끝이 a,t 이거나 g,c인 경우
            # 글자가 하나씩 줄었을때보다 2 증가
            dp[s][e] = dp[s + 1][e - 1] + 2

        for j in range(s, e):
            # j는 현재 확인 문자의 중간 부분을 도는 인덱스
            # 한바퀴 돌면서 가장 큰 걸 지정해준다.
            dp[s][e] = max(dp[s][e], dp[s][j] + dp[j + 1][e])

print(dp[0][len(dna) - 1])
```

## 접근방법

- 글자 수를 하나씩 늘려가면서, 양 끝을 체크하고, 가운데를 체크하는 순서로 진행
- 2개, 3개 ... 늘려가면서 dp 배열을 채우는 방식의 dp 문제
- 양끝이 a,t 이거나 , g,c일때만 그 안쪽의 문자보다 2를 더해주면 된다.

## 어려웠던 부분

- 처음에는 중간부분의 확인을 안해서 어려움을 겪었다.
- 백준 사이트 기준으로 python3에서는 시간초과이지만, pypy를 쓰면 돌아간다.

## 새로 알게 된 것

- 안쪽의 for문을 없앨 수 있는 방법이 있지 않을까 한번 더 생각해볼 만한 문제이다.
