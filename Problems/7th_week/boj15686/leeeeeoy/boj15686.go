package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	sc              = bufio.NewScanner(os.Stdin)
	n, m            int
	h               = [50][50]int{}
	chicken, person = make([]point, 0), make([]point, 0)
	selChicken      []point
	result          = 1 << 30
)

func main() {
	n, m = nextInt(), nextInt()
	selChicken = make([]point, m)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			h[i][j] = nextInt()
			if h[i][j] == 1 { //	집 위치 추가
				person = append(person, point{i, j})
			} else if h[i][j] == 2 { //	치킨 위치 추가
				chicken = append(chicken, point{i, j})
			}
		}
	}
	find(0, 0)
	fmt.Print(result)

}
func find(cs, k int) {
	if cs == m {
		sum := 0
		for _, h := range person {
			minDist := 1 << 30
			for i := 0; i < m; i++ {
				d := dis(selChicken[i], h)
				if minDist > d {
					minDist = d
				}
			}
			sum += minDist
		}
		if result > sum {
			result = sum
		}
		return
	}
	for i := k; i < len(chicken); i++ {
		selChicken[cs] = chicken[i]
		find(cs+1, i+1)
	}
}
func dis(d1, d2 point) int {
	return abs(d1.x-d2.x) + abs(d1.y-d2.y)
}

type point struct {
	x, y int
}

func minInt(a, b int) int {
	if a > b {
		return b
	}
	return a
}
func abs(a int) int {
	if a < 0 {
		return -1 * a
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
