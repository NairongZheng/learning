package utils

import "golang.org/x/exp/constraints"

func SelectedSort[T constraints.Ordered](nums []T) []T {
	for i := 0; i < len(nums); i++ {
		min_index := i
		for j := i + 1; j < len(nums); j++ {
			if nums[j] < nums[min_index] {
				min_index = j
			}
		}
		nums[i], nums[min_index] = nums[min_index], nums[i]
	}
	return nums
}
