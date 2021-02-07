package main

import (
	"fmt"
	"regexp"
	"strings"
)

func main() {
	fmt.Println(mostCommonWord(
		"Bob hit a ball, the hit BALL flew far after it was hit.",
		[]string{"hit"},
	))
	fmt.Println(mostCommonWord(
		"abc abc? abcd the jeff!",
		[]string{"abc", "abcd", "jeff"},
	))
}
func mostCommonWord(paragraph string, banned []string) string {
	paragraph = strings.ToLower(paragraph)
	re, _ := regexp.Compile("[,.!?;'']")
	paragraph = re.ReplaceAllString(paragraph, " ")
	paragraphs := strings.Split(paragraph, " ")

	m := make(map[string]int)
	b := make(map[string]bool)

	for _, ban := range banned {
		b[ban] = true
	}

	for _, word := range paragraphs {
		if _, ok := m[word]; ok {
			m[word]++
		} else {
			if _, ok := b[word]; !ok && strings.Trim(word, " ") != "" {
				m[word] = 1
			}
		}
	}
	max := 0
	answer := ""
	for word := range m {
		if m[word] > max {
			max = m[word]
			answer = word
		}
	}
	return answer
}
