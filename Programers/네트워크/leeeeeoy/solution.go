package main

import "fmt"

func main() {
	fmt.Println(solution(3, [][]int{
		{1, 1, 0},
		{1, 1, 0},
		{0, 0, 1},
	}))
	fmt.Println(solution(3, [][]int{
		{1, 1, 0},
		{1, 1, 1},
		{0, 1, 1},
	}))
}

var (
	check []bool
)

func solution(n int, computers [][]int) int {
	answer := 0
	check = make([]bool, n)

	for i := 0; i < n; i++ {
		if !check[i] {
			dfs(i, computers)
			answer++
		}
	}
	return answer
}
func dfs(i int, computers [][]int) {
	check[i] = true

	for k := 0; k < len(computers); k++ {
		if k != i && !check[k] && computers[i][k] == 1 {
			dfs(k, computers)
		}
	}
}
