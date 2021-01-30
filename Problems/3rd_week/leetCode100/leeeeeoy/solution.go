package main

import "fmt"

//TreeNode struct
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	fmt.Println(isSameTree(
		&TreeNode{1, &TreeNode{2, nil, nil}, &TreeNode{3, nil, nil}},
		&TreeNode{1, &TreeNode{2, nil, nil}, &TreeNode{3, nil, nil}}))
	fmt.Println(isSameTree(
		&TreeNode{1, &TreeNode{2, nil, nil}, nil},
		&TreeNode{1, nil, &TreeNode{2, nil, nil}}))
	fmt.Println(isSameTree(
		&TreeNode{1, &TreeNode{2, nil, nil}, &TreeNode{1, nil, nil}},
		&TreeNode{1, &TreeNode{1, nil, nil}, &TreeNode{2, nil, nil}}))
}
func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == q {
		return true
	}
	if (p != nil && q == nil) || (p == nil && q != nil) {
		return false
	}
	if p.Val != q.Val {
		return false
	}
	if isSameTree(p.Right, q.Right) && isSameTree(p.Left, q.Left) {
		return true
	}
	return false
}
