package main

import "fmt"

//TreeNode struct
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	fmt.Println(isSymmetric(
		&TreeNode{
			1,
			&TreeNode{
				2,
				&TreeNode{3, nil, nil},
				&TreeNode{4, nil, nil},
			},
			&TreeNode{
				2,
				&TreeNode{4, nil, nil},
				&TreeNode{4, nil, nil},
			},
		}))
	fmt.Println(isSymmetric(
		&TreeNode{
			1,
			&TreeNode{
				2,
				nil,
				&TreeNode{3, nil, nil},
			},
			&TreeNode{
				2,
				nil,
				&TreeNode{3, nil, nil},
			},
		}))
}

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	if check := check(root.Left, root.Right); check {
		return true
	}
	return false
}
func check(left, right *TreeNode) bool {
	if left == nil && right == nil {
		return true
	}
	if left == nil || right == nil {
		return false
	}
	if left.Val != right.Val {
		return false
	}
	if check(left.Left, right.Right) && check(left.Right, right.Left) {
		return true
	}
	return false
}
