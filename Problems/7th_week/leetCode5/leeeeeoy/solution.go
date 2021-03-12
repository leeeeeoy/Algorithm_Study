package main

import "fmt"

func main() {
	fmt.Println(longestPalindrome("babad"))
	fmt.Println(longestPalindrome("cbbd"))
	fmt.Println(longestPalindrome("a"))
	fmt.Println(longestPalindrome("ac"))
}

var (
	index int
	max   int
)

func longestPalindrome(s string) string {
	if len(s) < 2 {
		return s
	}
	for i := 0; i < len(s)-1; i++ {
		find(s, i, i)
		find(s, i, i+1)
	}
	answer := s[index : index+max]
	return answer
}
func find(s string, i, j int) {
	for i >= 0 && j < len(s) && s[i] == s[j] {
		i--
		j++
	}
	if max < j-i-1 {
		index = i + 1
		max = j - i - 1
	}
}
