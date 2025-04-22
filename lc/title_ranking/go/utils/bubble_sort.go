package utils

import (
	"golang.org/x/exp/constraints"
)

// 泛型冒泡排序：支持 int、float64、string 等有序类型
func BubbleSort[T constraints.Ordered](nums []T) []T {
	n := len(nums)
	for i := 0; i < n-1; i++ {
		swapped := false
		for j := 0; j < n-1-i; j++ {
			if nums[j] > nums[j+1] {
				nums[j], nums[j+1] = nums[j+1], nums[j]
				swapped = true
			}
		}
		if !swapped {
			break
		}
	}
	return nums
}
