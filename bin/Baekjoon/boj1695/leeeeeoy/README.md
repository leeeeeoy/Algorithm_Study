# 풀이

## 접근방법

```go
// start부터 end까지의 헤딩 수열을 만드는데 필요한 최소 갯수
dp[start][end]
```

- start >= end 일 경우 종료 -> 탐색 범위 벗어남
- 이미 dp값이 채워졌으면 해당 값 리턴
- start와 end 지점의 수가 같을 경우 start+1, end-1 비교
- 다를 경우 start, end-1의 경우와 start + 1, end 비교
- 위 비교 값들 중 최솟값 저장

## 어려웠던 부분

- 문자가 다를 경우 해당 인덱스 조절 후 번호를 넣어야 하므로 함수값 + 1을 해줘야 함

## 새로 알게 된 것

- 새롭게 알게 된 내용 정리