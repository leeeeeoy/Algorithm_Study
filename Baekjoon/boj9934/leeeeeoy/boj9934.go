package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

var (
	sc    = bufio.NewScanner(os.Stdin)
	b     [1024]int
	check [11][]int
)

func main() {
	k := nextInt()
	size := (int)(math.Pow(2, (float64)(k)) - 1)
	for i := 1; i <= size; i++ {
		b[i] = nextInt()
	}
	find(1, size, 1)

	for i := 1; i <= k; i++ {
		for _, num := range check[i] {
			fmt.Print(num, " ")
		}
		fmt.Println()
	}
}
func find(start, end, level int) {
	mid := (start + end) / 2
	check[level] = append(check[level], b[mid])
	if start == end {
		return
	}
	find(start, mid-1, level+1)
	find(mid+1, end, level+1)
}
func nextInt() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}
func init() {
	sc.Split(bufio.ScanWords)
}
