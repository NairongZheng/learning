package utils

import "golang.org/x/exp/constraints"

func Merge[T constraints.Ordered](firstList []T, secondList []T) []T {
	firstIndex := 0
	secondIndex := 0
	result := []T{}
	for firstIndex < len(firstList) && secondIndex < len(secondList) {
		if firstList[firstIndex] < secondList[secondIndex] {
			result = append(result, firstList[firstIndex])
			firstIndex++
		} else {
			result = append(result, secondList[secondIndex])
			secondIndex++
		}
	}
	result = append(result, firstList[firstIndex:]...)
	result = append(result, secondList[secondIndex:]...)
	return result
}

func MergeSort[T constraints.Ordered](nums []T) []T {
	n := len(nums)
	if n <= 1 {
		return nums
	}
	pivotIndex := n / 2
	firstList := MergeSort(nums[:pivotIndex])
	secondList := MergeSort(nums[pivotIndex:])
	return Merge(firstList, secondList)
}
