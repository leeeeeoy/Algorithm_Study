package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

var (
	sc       = bufio.NewScanner(os.Stdin)
	n        int
	p        []int   //	사람 수
	g        [][]int //	구역
	visit    []bool  //	방문 여부 check
	selected []bool  //	선택한 구역인지 아닌지 check
	answer   = math.MaxInt16
)

func main() {
	n = nextInt()
	p = make([]int, n+1)
	for i := 1; i <= n; i++ {
		p[i] = nextInt()
	}
	selected = make([]bool, n+1)
	g = make([][]int, n+1)
	for i := 1; i <= n; i++ {
		a := nextInt()
		g[i] = make([]int, 0)
		for j := 0; j < a; j++ {
			nn := nextInt()
			g[nn] = append(g[nn], i)
			g[i] = append(g[i], nn)
		}
	}

	dfs(1, 0)

	if answer == math.MaxInt16 {
		fmt.Print(-1)
	} else {
		fmt.Print(answer)
	}
}

func dfs(start, depth int) {
	if depth >= 1 && checkCon() {
		cal()
	}

	for i := start; i <= n; i++ {
		if selected[i] {
			continue
		}
		selected[i] = true
		dfs(i+1, depth+1)
		selected[i] = false
	}
}

func cal() {
	a, b := 0, 0
	for i := 1; i <= n; i++ {
		if selected[i] {
			a += p[i]
		} else {
			b += p[i]
		}
	}
	answer = minInt(answer, absInt(a-b))
}

func isCon(cur []int, isSel bool) bool {
	q := make([]int, 0)
	visit = make([]bool, n+1)
	visit[cur[0]] = true
	q = append(q, cur[0])
	count := 1

	for len(q) > 0 {
		v := q[0]
		q = q[1:]

		for _, val := range g[v] {
			if selected[val] != isSel || visit[val] {
				continue
			}
			count++
			visit[val] = true
			q = append(q, val)
		}
	}

	if len(cur) == count {
		return true
	}
	return false
}

func checkCon() bool {
	a := make([]int, 0)
	b := make([]int, 0)

	for i := 1; i <= n; i++ {
		if selected[i] {
			a = append(a, i)
		} else {
			b = append(b, i)
		}
	}
	if len(a) == 0 || len(b) == 0 {
		return false
	}
	if !isCon(a, true) {
		return false
	}
	if !isCon(b, false) {
		return false
	}
	return true
}

func minInt(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func absInt(a int) int {
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
