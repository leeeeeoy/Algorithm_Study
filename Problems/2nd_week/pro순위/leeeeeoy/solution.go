package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Print(solution(5, [][]int{
		{4, 3},
		{4, 2},
		{3, 2},
		{1, 2},
		{2, 5},
	}))
}

var (
	g [101][101]int
)

func solution(n int, results [][]int) int {
	answer := 0

	for i := 1; i <= n; i++ {
		for j := 1; j <= n; j++ {
			g[i][j] = math.MaxInt32
		}
	}
	for i := 0; i < len(results); i++ {
		win := results[i][0]
		lose := results[i][1]
		g[win][lose] = 1
		g[lose][win] = 0
	}

	for t := 1; t <= n; t++ {
		for i := 1; i <= n; i++ {
			for j := 1; j <= n; j++ {
				if g[i][j] == math.MaxInt32 {
					if g[i][t] == 1 && g[t][j] == 1 {
						g[i][j] = 1
					}
					if g[i][t] == 0 && g[t][j] == 0 {
						g[i][j] = 0
					}
				}
			}
		}
	}

	for i := 1; i <= n; i++ {
		check := false
		for j := 1; j <= n; j++ {
			if i != j && g[i][j] == math.MaxInt32 {
				check = true
				break
			}
		}

		if !check {
			answer++
		}
	}

	return answer
}
