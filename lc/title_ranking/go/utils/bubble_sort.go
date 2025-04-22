package utils

import (
	"golang.org/x/exp/constraints"
)

// 泛型冒泡排序：支持 int、float64、string 等有序类型
func BubbleSort[T constraints.Ordered](arr []T) []T {
	n := len(arr)
	for i := 0; i < n-1; i++ {
		swapped := false
		for j := 0; j < n-1-i; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = true
			}
		}
		if !swapped {
			break
		}
	}
	return arr
}
