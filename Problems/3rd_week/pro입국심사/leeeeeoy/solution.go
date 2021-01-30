package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(solution(6, []int{7, 10}))
}
func solution(n int, times []int) int {
	sort.Ints(times)
	left, right, mid := 0, times[len(times)-1]*n, 0
	answer := right

	for left <= right {
		check := 0
		mid = (left + right) / 2
		for _, time := range times {
			check += mid / time
		}

		if check < n {
			left = mid + 1
		} else {
			if answer >= mid {
				answer = mid
			}
			right = mid - 1
		}
	}
	return answer
}
