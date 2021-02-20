package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(solution([][]string{{"ICN", "JFK"}, {"HND", "IAD"}, {"JFK", "HND"}}))
	fmt.Println(solution([][]string{{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"}, {"ATL", "SFO"}}))
}

var (
	answer []string
	check  []bool
	count  int
)

func solution(tickets [][]string) []string {
	check = make([]bool, len(tickets))
	sort.Slice(tickets, func(i, j int) bool {
		return tickets[i][1] < tickets[j][1]
	})
	dfs("ICN", tickets, 0)
	return answer

}
func dfs(tmp string, tickets [][]string, cnt int) bool {
	answer = append(answer, tmp)
	if cnt == len(tickets) {
		return true
	}
	for i := 0; i < len(tickets); i++ {
		if tickets[i][0] == tmp && !check[i] {
			check[i] = true
			visit := dfs(tickets[i][1], tickets, cnt+1)
			if visit {
				return true
			}
			check[i] = false
		}
	}
	answer = answer[:len(answer)-1]
	return false
}
