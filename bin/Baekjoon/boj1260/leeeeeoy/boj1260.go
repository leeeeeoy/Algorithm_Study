package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var (
	sc      = bufio.NewScanner(os.Stdin)
	n, m, v int
	l       [][]int
	check   []bool
)

func main() {
	n, m, v = nextInt(), nextInt(), nextInt()
	l = make([][]int, n+1)
	for i := 1; i < n+1; i++ {
		l[i] = make([]int, 0)
	}
	for i := 0; i < m; i++ {
		u, v := nextInt(), nextInt()
		l[u] = append(l[u], v)
		l[v] = append(l[v], u)
	}
	for i := 1; i < n+1; i++ {
		sort.Ints(l[i])
	}

	check = make([]bool, n+1)
	dfs(v)
	fmt.Println()
	check = make([]bool, n+1)
	bfs(v)
}
func dfs(node int) {
	if check[node] {
		return
	}
	check[node] = true
	fmt.Print(node, " ")
	for _, n := range l[node] {
		if !check[n] {
			dfs(n)
		}
	}
}
func bfs(start int) {
	q := make([]int, 0)
	q = append(q, start)
	check[start] = true

	for len(q) > 0 {
		x := q[0]
		q = q[1:]
		fmt.Print(x, " ")
		for _, n := range l[x] {
			if !check[n] {
				check[n] = true
				q = append(q, n)
			}
		}
	}
}
func nextInt() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}
func init() {
	sc.Split(bufio.ScanWords)
}
