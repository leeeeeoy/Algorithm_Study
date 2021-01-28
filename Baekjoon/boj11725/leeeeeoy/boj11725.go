package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	sc      = bufio.NewScanner(os.Stdin)
	parents [100001]int
	list    [][]int
	check   [100001]bool
	n       int
)

func main() {
	n = nextInt()
	list = make([][]int, n+1)
	for i := 1; i < n; i++ {
		a, b := nextInt(), nextInt()
		list[a] = append(list[a], b)
		list[b] = append(list[b], a)
	}
	dfs(1)
	for i := 2; i <= n; i++ {
		fmt.Println(parents[i])
	}
}
func dfs(index int) {
	check[index] = true
	for _, i := range list[index] {
		if !check[i] {
			parents[i] = index
			dfs(i)
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
