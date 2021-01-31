package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	sc        = bufio.NewScanner(os.Stdin)
	n, answer int
	tree      [][]int
	check     []bool
)

func main() {
	n = nextInt()
	tree = make([][]int, n+1)
	check = make([]bool, n+1)
	for i := 1; i < n; i++ {
		a, b := nextInt(), nextInt()
		tree[a] = append(tree[a], b)
		tree[b] = append(tree[b], a)
	}
	dfs(1, 0)
	if answer%2 == 0 {
		fmt.Print("No")
	} else {
		fmt.Print("Yes")
	}
}
func dfs(node, count int) {
	check[node] = true
	for _, next := range tree[node] {
		if !check[next] {
			dfs(next, count+1)
		}
	}
	if node != 1 && len(tree[node]) == 1 {
		answer += count
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
