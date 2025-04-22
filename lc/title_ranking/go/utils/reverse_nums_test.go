package utils

import (
	"testing"
)

func TestReverse(t *testing.T) {
	tests := []struct {
		name     string
		input    []int
		expected []int
	}{
		{"Reverse multiple", []int{1, 2, 3, 4, 5}, []int{5, 4, 3, 2, 1}},
		{"Reverse single", []int{1}, []int{1}},
		{"Reverse empty", []int{}, []int{}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Logf("Input before reverse: %v", tt.input)

			Reverse(tt.input)

			t.Logf("Input after reverse:  %v", tt.input)
			t.Logf("Expected result:     %v", tt.expected)

			for i, v := range tt.input {
				if v != tt.expected[i] {
					t.Errorf("At index %d: expected %d, got %d", i, tt.expected[i], v)
				}
			}
		})
	}
}
