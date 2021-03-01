package main

import "fmt"

func main() {
	fmt.Println(maxProfit([]int{7, 1, 5, 3, 6, 4}))
	fmt.Println(maxProfit([]int{7, 6, 4, 3, 1}))
}
func maxProfit(prices []int) int {
	answer := 0
	tmp := prices[0]
	for i := 1; i < len(prices); i++ {
		if tmp > prices[i] {
			tmp = prices[i]
			continue
		}
		if prices[i]-tmp > answer {
			answer = prices[i] - tmp
		}
	}
	return answer
}
