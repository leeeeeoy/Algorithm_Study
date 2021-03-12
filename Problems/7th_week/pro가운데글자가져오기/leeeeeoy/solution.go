package main

import "fmt"

func main() {
	fmt.Println(solution("abcde"))
	fmt.Println(solution("qwer"))
}
func solution(s string) string {
	var answer string
	if len(s)%2 == 0 {
		answer = s[len(s)/2-1 : len(s)/2+1]
	} else {
		answer = string(s[len(s)/2])
	}
	return answer
}
