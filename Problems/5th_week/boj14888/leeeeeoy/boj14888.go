package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

var (
	sc      = bufio.NewScanner(os.Stdin)
	n       int
	numbers []int
	op      [4]int
	max     = -1 * math.MaxInt64
	min     = math.MaxInt64
)

func main() {
	n = nextInt()
	numbers = make([]int, n)
	for i := 0; i < n; i++ {
		numbers[i] = nextInt()
	}
	for i := 0; i < 4; i++ {
		op[i] = nextInt()
	}
	find(numbers[0], 1)
	fmt.Println(max)
	fmt.Print(min)
}
func find(sum, index int) {
	if index == n {
		if max < sum {
			max = sum
		}
		if min > sum {
			min = sum
		}
		return
	}
	for i := 0; i < 4; i++ {
		if op[i] > 0 {
			op[i]--
			if i == 0 {
				find(sum+numbers[index], index+1)
			}
			if i == 1 {
				find(sum-numbers[index], index+1)
			}
			if i == 2 {
				find(sum*numbers[index], index+1)
			}
			if i == 3 {
				find(sum/numbers[index], index+1)
			}
			op[i]++
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
