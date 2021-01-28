package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	br  = bufio.NewReader(os.Stdin)
	bw  = bufio.NewWriter(os.Stdout)
	str = make(map[string]int)
)

func main() {
	defer bw.Flush()
	var n, m int
	fmt.Fscanln(br, &n, &m)
	for i := 0; i < n; i++ {
		s, _ := br.ReadString('\n')
		str[s] = 1
	}
	count := 0
	for i := 0; i < m; i++ {
		ss, _ := br.ReadString('\n')
		_, check := str[ss]
		if check {
			count++
		}
	}
	fmt.Fprint(bw, count)
}
