package utils

import "golang.org/x/exp/constraints"

func SelectedSort[T constraints.Ordered](arr []T) []T {
	for i := 0; i < len(arr); i++ {
		min_index := i
		for j := i + 1; j < len(arr); j++ {
			if arr[j] < arr[min_index] {
				min_index = j
			}
		}
		arr[i], arr[min_index] = arr[min_index], arr[i]
	}
	return arr
}
