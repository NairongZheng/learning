package utils

import "golang.org/x/exp/constraints"

func ShellSort[T constraints.Ordered](nums []T) []T {
	gap := len(nums) / 2
	for gap >= 1 {
		for i := gap; i < len(nums); i++ {
			j := i
			for j >= gap {
				if nums[j] < nums[j-gap] {
					nums[j], nums[j-gap] = nums[j-gap], nums[j]
					j -= gap
				} else {
					break
				}
			}
		}
		gap /= 2
	}
	return nums
}
