package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var (
	br  = bufio.NewReader(os.Stdin)
	bw  = bufio.NewWriter(os.Stdout)
	s   string
	str []string
	st  = make([]string, 0)
)

func main() {
	defer bw.Flush()
	fmt.Fscan(br, &s)
	if len(s)%2 == 1 {
		fmt.Print(0)
	} else {
		str = strings.Split(s, "")
		fmt.Fprint(bw, find())
	}
}
func find() int {
	result, cur := 0, 1
	for i := 0; i < len(str); i++ {
		if str[i] == "(" {
			cur *= 2
			st = append(st, str[i])
		} else if str[i] == "[" {
			cur *= 3
			st = append(st, str[i])
		} else if str[i] == ")" {
			if len(st) == 0 || st[len(st)-1] != "(" {
				result = 0
				break
			}
			if str[i-1] == "(" {
				result += cur
			}
			st = st[:len(st)-1]
			cur /= 2
		} else if str[i] == "]" {
			if len(st) == 0 || st[len(st)-1] != "[" {
				result = 0
				break
			}
			if str[i-1] == "[" {
				result += cur
			}
			st = st[:len(st)-1]
			cur /= 3
		}
	}
	return result
}
