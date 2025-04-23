package utils

import "golang.org/x/exp/constraints"

func QuickSortRecursion1[T constraints.Ordered](nums []T, head int, tail int) []T {
	// 原地快排，空间复杂度O(logn)（递归栈）
	if head >= tail {
		return nums
	}

	pivot := nums[head]
	left := head
	right := tail

	for left != right {
		for left < right && nums[right] >= pivot {
			right--
		}
		nums[left] = nums[right]

		for left < right && nums[left] <= pivot {
			left++
		}
		nums[right] = nums[left]
	}

	nums[left] = pivot

	QuickSortRecursion1(nums, head, left-1)
	QuickSortRecursion1(nums, left+1, tail)

	return nums
}

func QuickSortRecursion2[T constraints.Ordered](nums []T) []T {
	// 原地快排，空间复杂度O(n)（使用额外空间）
	if len(nums) < 2 {
		return nums
	}
	pivot := nums[0]
	leftList := []T{}
	rightList := []T{}
	for _, v := range nums[1:] {
		if v <= pivot {
			leftList = append(leftList, v)
		} else {
			rightList = append(rightList, v)
		}
	}
	sortedLeft := QuickSortRecursion2(leftList)
	sortedRight := QuickSortRecursion2(rightList)

	result := append(sortedLeft, pivot)
	result = append(result, sortedRight...)
	return result
}

func QuickSort[T constraints.Ordered](nums []T) []T {
	// // 方法一：原地快排
	// result := QuickSortRecursion1(nums, 0, len(nums)-1)
	// 方法二：非原地快排
	result := QuickSortRecursion2(nums)
	return result
}
