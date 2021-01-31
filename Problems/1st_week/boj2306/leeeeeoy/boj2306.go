package main

import (
	"fmt"
)

var (
	dna string
	dp  [500][500]int
)

//	at, gc -> KOI
func main() {
	fmt.Scan(&dna)
	for i := 0; i < len(dna); i++ {
		for j := 0; j < len(dna); j++ {
			dp[i][j] = -1
		}
	}
	answer := find(0, len(dna)-1)
	fmt.Print(answer)
}
func find(start, end int) int {
	if start >= end {
		return 0
	}
	if dp[start][end] != -1 {
		return dp[start][end]
	}
	cur := -1
	for i := start; i < end; i++ {
		cur = maxInt(cur, find(start, i)+find(i+1, end))
	}
	if (dna[start] == 'a' && dna[end] == 't') || (dna[start] == 'g' && dna[end] == 'c') {
		cur = maxInt(cur, find(start+1, end-1)+2)
	}
	dp[start][end] = cur
	return cur
}
func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}
