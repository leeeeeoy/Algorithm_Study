package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
)

type pair struct {
	x int
	y int
}

var (
	sc = bufio.NewScanner(os.Stdin)
)

func main() {
	n, m, s := nextInt(), nextInt(), nextInt()
	g := make([][]pair, n+1)
	for i := 0; i < m; i++ {
		a, b, c := nextInt(), nextInt(), nextInt()
		g[a] = append(g[a], pair{b, c})
	}

	q := queue{}
	v := make([]int, n+1)
	heap.Push(&q, &pair{s, 1})
	v[s] = 1

	for q.Len() > 0 {
		cur := heap.Pop(&q).(*pair)

		if v[cur.x] < cur.y {
			continue
		}

		for _, next := range g[cur.x] {
			if v[next.x] == 0 || v[next.x] > v[cur.x]+next.y {
				v[next.x] = v[cur.x] + next.y
				heap.Push(&q, &pair{next.x, v[next.x]})
			}
		}
	}

	for i := 1; i <= n; i++ {
		if v[i] == 0 {
			fmt.Println("INF")
		} else {
			fmt.Println(v[i] - 1)
		}
	}

}

type queue []*pair

func (q queue) Len() int {
	return len(q)
}
func (q queue) Less(i, j int) bool {
	return q[i].y < q[j].y
}
func (q queue) Swap(i, j int) {
	q[i], q[j] = q[j], q[i]
}
func (q *queue) Push(x interface{}) {
	*q = append(*q, x.(*pair))
}
func (q *queue) Pop() interface{} {
	old := *q
	n := len(old)
	item := old[n-1]
	*q = old[0 : n-1]
	return item
}
func nextInt() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}
func init() {
	sc.Split(bufio.ScanWords)
}
