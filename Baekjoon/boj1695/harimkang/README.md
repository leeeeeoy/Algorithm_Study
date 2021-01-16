# 풀이

```python
# input을 받는 코드 : N
N = int(input())
num_list = list(map(int, input().split()))

# i, j자리의 숫자를 비교해서 같으면 한칸씩 줄이고, 다르면 1개를 추가해야한다는 의미로, +1 해주고 한쪽만 줄이는 방식
dp = [[None for _ in range(N)] for _ in range(N)]


def palindrome(i, j):
    if dp[i][j] is not None:
        return dp[i][j]
    if i >= j:
        dp[i][j] = 0
        return 0
    else:
        if num_list[i] == num_list[j]:
            dp[i][j] = palindrome(i + 1, j - 1)
        else:
            dp[i][j] = min(palindrome(i + 1, j), palindrome(i, j - 1)) + 1

        return dp[i][j]


if num_list == num_list[::-1]:
    print(0)
else:
    for i in range(0, N - 1):
        for j in range(i + 1, N):
            palindrome(i, j)

    print(dp[0][N - 1])
```

## 접근방법

- dp와 재귀를 섞어서 쓰는 방식으로 접근하였다.
- i는 시작점, j는 i의 다음 자리부터 끝까지 순환하면서 palindrome를 체크한다.
- 이미 채워진 dp에 대해서는 해당 값을 리턴하며, i>=j의 경우에는 0을 대입한다.
- 숫자 비교시, 같으면 i+1, j-1로 진행하며, 다르면 한쪽만 이동한 경우들 중 최소값에 1을 더한다.

## 어려웠던 부분

- 재귀와 관련된 초과 에러가 나는데 이 에러가 백준 사이트 기준으로 파이썬에서만 나는듯 하다.

## 새로 알게 된 것

- 시간이 된다면, 재귀를 없애는 방법을 한번 더 생각해볼 필요가 있다.
