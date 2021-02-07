package main

import "fmt"

func main() {
	fmt.Println(canJump([]int{2, 3, 1, 1, 4}))
	fmt.Println(canJump([]int{3, 2, 1, 0, 4}))
	fmt.Println(canJump([]int{3, 0, 8, 2, 0, 0, 1}))
	fmt.Println(canJump([]int{2, 0}))
	fmt.Println(canJump([]int{0, 2, 3}))

}
func canJump(nums []int) bool {
	count := len(nums) - 1
	for i := len(nums) - 1; i >= 0; i-- {
		if i+nums[i] >= count {
			count = i
		}
	}
	if count == 0 {
		return true
	}
	return false
}
