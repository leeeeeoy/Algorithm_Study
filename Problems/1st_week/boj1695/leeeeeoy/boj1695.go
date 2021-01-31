package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

var (
	sc     = bufio.NewScanner(os.Stdin)
	p      [5001]int
	dp     [5001][5001]int
	answer int
)

func main() {
	n := nextInt()
	for i := 0; i < n; i++ {
		p[i] = nextInt()
	}
	answer = find(0, n-1)
	fmt.Print(answer)

}
func find(start, end int) int {
	if start >= end {
		return 0
	}
	if dp[start][end] != 0 {
		return dp[start][end]
	}
	cur := math.MaxInt32

	if p[start] == p[end] {
		cur = minInt(cur, find(start+1, end-1))
	} else {
		cur = minInt(find(start, end-1)+1, find(start+1, end)+1)
	}

	dp[start][end] = cur
	return cur
}
func minInt(a, b int) int {
	if a > b {
		return b
	}
	return a
}
func nextInt() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}
func init() {
	sc.Split(bufio.ScanWords)
}
