package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	sc    = bufio.NewScanner(os.Stdin)
	maap  [][]int
	check []bool
	count int
)

func main() {
	n, m := nextInt(), nextInt()
	maap = make([][]int, n+1)
	check = make([]bool, n+1)
	for i := 0; i < m; i++ {
		a, b := nextInt(), nextInt()
		maap[a] = append(maap[a], b)
		maap[b] = append(maap[b], a)
	}

	for i := 1; i <= n; i++ {
		if !check[i] {
			bfs(i)
			count++
		}
	}

	fmt.Print(count)
}
func bfs(v int) {
	q := make([]int, 0)
	q = append(q, v)
	check[v] = true

	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		for _, node := range maap[cur] {
			if !check[node] {
				check[node] = true
				q = append(q, node)
			}
		}
	}
}

// func dfs(v int) {
// 	check[v] = true
// 	for _, node := range maap[v] {
// 		if check[node] {
// 			dfs(node)
// 		}
// 	}
// }
func nextInt() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}
func init() {
	sc.Split(bufio.ScanWords)
}
