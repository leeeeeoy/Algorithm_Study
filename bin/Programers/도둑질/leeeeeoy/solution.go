package main

import "fmt"

func main() {
	fmt.Print(solution([]int{1, 2, 3, 1}))
}

var (
	dp [1000001][2]int
)

func solution(money []int) int {
	dp[0][0] = money[0]
	dp[1][0] = maxInt(money[0], money[1])

	for i := 2; i < len(money)-1; i++ {
		dp[i][0] = maxInt(dp[i-2][0]+money[i], dp[i-1][0])
	}
	dp[1][1] = money[1]
	for i := 2; i < len(money); i++ {
		dp[i][1] = maxInt(dp[i-2][1]+money[i], dp[i-1][1])
	}
	answer := maxInt(dp[len(money)-2][0], dp[len(money)-1][1])
	return answer
}
func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}
