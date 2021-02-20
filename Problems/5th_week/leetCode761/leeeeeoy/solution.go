package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(makeLargestSpecial("11011000"))
	fmt.Println(makeLargestSpecial("11100010"))
}
func makeLargestSpecial(S string) string {
	var answer string
	o, z := 0, 0
	tmp := []string{}
	s := 0
	for i := 0; i < len(S); i++ {
		if S[i] == '1' {
			o++
		} else {
			z++
		}
		if o == z {
			tmp = append(tmp, "1"+makeLargestSpecial(S[s+1:i])+"0")
			s = i + 1
			o, z = 0, 0
		}
	}
	sort.Strings(tmp)

	for i := len(tmp) - 1; i >= 0; i-- {
		answer += tmp[i]
	}
	return answer
}
