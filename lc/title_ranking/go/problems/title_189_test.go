package problems

import (
	"reflect"
	"testing"
)

func TestRotate(t *testing.T) {
	tests := []struct {
		input    []int
		k        int
		expected []int
	}{
		{[]int{1, 2, 3, 4, 5, 6, 7}, 3, []int{5, 6, 7, 1, 2, 3, 4}},
		{[]int{1, 2, 3, 4, 5, 6}, 2, []int{5, 6, 1, 2, 3, 4}},
		{[]int{1}, 3, []int{1}},
		{[]int{}, 3, []int{}},
	}

	for i, tt := range tests {

		Rotate(tt.input, tt.k)

		t.Logf("Input after reverse:  %v", tt.input)

		if !reflect.DeepEqual(tt.input, tt.expected) {
			t.Errorf("Test %d failed: expected %v, got %v", i, tt.expected, tt.input)
		}
	}
}
