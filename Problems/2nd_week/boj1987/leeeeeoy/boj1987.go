package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	br      = bufio.NewReader(os.Stdin)
	bw      = bufio.NewWriter(os.Stdout)
	b       []string
	dx      = [4]int{1, -1, 0, 0}
	dy      = [4]int{0, 0, 1, -1}
	check   [27]bool
	answer  = 1
	curStep = 1
	r, c    int
)

func main() {
	defer bw.Flush()
	fmt.Fscanln(br, &r, &c)
	b = make([]string, 0)
	for i := 0; i < r; i++ {
		str, _ := br.ReadString('\n')
		b = append(b, str)
	}
	dfs(0, 0)
	fmt.Fprint(bw, answer)
}
func dfs(x, y int) {
	cur := int(b[x][y] - 65)
	check[cur] = true

	for i := 0; i < 4; i++ {
		curX := dx[i] + x
		curY := dy[i] + y

		if curX >= 0 && curX < r && curY >= 0 && curY < c {
			next := int(b[curX][curY] - 65)
			if !check[next] {
				curStep++
				answer = maxInt(answer, curStep)
				dfs(curX, curY)
			}
		}
	}

	curStep--
	check[cur] = false
}
func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}
