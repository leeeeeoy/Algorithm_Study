package main

import "fmt"

func main() {
	fmt.Println(findJudge(2, [][]int{{1, 2}}))
	fmt.Println(findJudge(3, [][]int{{1, 3}, {2, 3}}))
	fmt.Println(findJudge(3, [][]int{{1, 3}, {2, 3}, {2, 3}}))
	fmt.Println(findJudge(3, [][]int{{1, 2}, {2, 3}}))
	fmt.Println(findJudge(4, [][]int{{1, 3}, {1, 4}, {2, 3}, {2, 4}, {4, 3}}))
}

func findJudge(N int, trust [][]int) int {
	m := make([]int, N+1)

	for i := 0; i < len(trust); i++ {
		from := trust[i][0]
		to := trust[i][1]
		m[to]++
		m[from] = -N
	}

	answer := -1
	for i := 1; i <= N; i++ {
		if m[i] == N-1 {
			if answer == -1 {
				answer = i
			} else {
				return -1
			}
		}
	}
	return answer
}
