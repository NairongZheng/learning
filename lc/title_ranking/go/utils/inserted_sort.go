package utils

import "golang.org/x/exp/constraints"

func InsertedSort[T constraints.Ordered](nums []T) []T {
	for i := 1; i < len(nums); i++ {
		j := i
		for j > 0 {
			if nums[j] < nums[j-1] {
				nums[j], nums[j-1] = nums[j-1], nums[j]
				j--
			} else {
				break
			}
		}
	}
	return nums
}
