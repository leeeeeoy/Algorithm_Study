# 풀이

```python
def solution(money):

    answer = []

    # 첫번째 집에 방문하는 경우
    dp = [0 for _ in money]
    dp[0] = dp[1] = money[0]
    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    answer.append(max(dp))

    # 첫번째를 안가고 두번째를 방문하는 경우
    dp[0] = 0
    dp[1] = money[1]
    for i in range(2, len(money)):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    answer.append(max(dp))

    # 첫번째 두번째 모두 안가는 경우
    dp[0] = dp[1] = 0
    for i in range(2, len(money)):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    answer.append(max(dp))

    return max(answer)
```

## 접근방법

- DP 구현 -> 순서대로 크기를 비교하며 현 상태의 최댓값을 계산하기
- 경우의 수를 큰 범위에서 잡고 시작
- 첫번째 집을 방문하는 경우 마지막 집을 못가기 때문에 3가지 경우로 나눔
  1. 첫번째 집에 방문하는 경우 -> 마지막 집은 제외
  2. 첫번째를 안가고 두번째를 방문하는 경우 -> 마지막 집 포함
  3. 첫번째 두번째 모두 안가는 경우 -> 마지막 집 포함
- 3가지 경우 중, 최대값이 정답

## 어려웠던 부분

- 경우의 수를 3가지 생각을 해야하는데 2가지만을 생각하여서 처음에는 오답이 생겼다.
- 첫번째 집과 두번째 집을 모두 안가는 경우에도 정답이 발생할 수 있다. (원형 모양이라서 생기는 경우)

## 새로 알게 된 것

- 원형 모양에 대한 경우의 수
