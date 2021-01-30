package main

import "fmt"

func main() {
	fmt.Print(solution(6, [][]int{
		{3, 6},
		{4, 3},
		{3, 2},
		{1, 3},
		{1, 2},
		{2, 4},
		{5, 2},
	}))
}

var (
	dis   []int
	check [][]bool
	node  []int
	max   int
)

func solution(n int, edge [][]int) int {
	answer := 0

	dis = make([]int, n+1)
	check = make([][]bool, n+1)
	for i := 1; i <= n; i++ {
		check[i] = make([]bool, n+1)
	}

	for i := 0; i < len(edge); i++ {
		check[edge[i][0]][edge[i][1]] = true
		check[edge[i][1]][edge[i][0]] = true
	}

	node = append(node, 1)
	for len(node) > 0 {
		cur := node[0]
		node = node[1:]

		for i := 2; i <= n; i++ {
			if dis[i] == 0 && check[cur][i] {
				dis[i] = dis[cur] + 1
				node = append(node, i)
				max = maxInt(max, dis[i])
			}
		}
	}

	for _, num := range dis {
		if max == num {
			answer++
		}
	}
	return answer
}
func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}
