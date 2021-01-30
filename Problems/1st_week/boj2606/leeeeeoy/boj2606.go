package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	sc    = bufio.NewScanner(os.Stdin)
	n, k  int
	check []bool
	b     [][]int
	count int
)

func main() {
	n, k = nextInt(), nextInt()
	check = make([]bool, n+1)
	b = make([][]int, n+1)
	for i := 1; i < n+1; i++ {
		b[i] = make([]int, n+1)
	}
	for i := 0; i < k; i++ {
		u, v := nextInt(), nextInt()
		b[u][v] = 1
		b[v][u] = 1
	}
	dfs(1)
	fmt.Print(count)
}
func dfs(node int) {
	check[node] = true

	for i := 1; i < n+1; i++ {
		if b[node][i] == 1 && !check[i] {
			dfs(i)
			count++
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
