package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(solution("hit", "cog", []string{"hot", "dot", "dog", "lot", "log", "cog"}))
	fmt.Println(solution("hit", "cog", []string{"hot", "dot", "dog", "lot", "log"}))
}

var (
	answer = math.MaxInt16
	cur    string
	check  = make([]bool, 50)
)

func solution(begin string, target string, words []string) int {
	cur = target
	dfs(begin, words, 0)
	if answer == math.MaxInt16 {
		answer = 0
	}
	return answer
}
func dfs(begin string, words []string, count int) {
	if cur == begin {
		if answer > count {
			answer = count
		}
		return
	}

	for i := 0; i < len(words); i++ {
		tmp := 0
		for j := 0; j < len(words[i]); j++ {
			if begin[j] != words[i][j] {
				tmp++
			}
			if tmp == 2 {
				break
			}
		}

		if tmp == 1 {
			if check[i] == false {
				check[i] = true
				dfs(words[i], words, count+1)
				check[i] = false
			}
		}
	}
}
