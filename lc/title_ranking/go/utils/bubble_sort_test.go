package utils

import (
	"reflect"
	"testing"
)

func TestBubbleSortInt(t *testing.T) {
	input := []int{5, 3, 1, 4, 2}
	expected := []int{1, 2, 3, 4, 5}
	result := BubbleSort(input)
	t.Logf("res:  %v", result)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("int: expected %v, got %v", expected, result)
	}
}

func TestBubbleSortFloat(t *testing.T) {
	input := []float64{3.14, 2.71, -1.0, 0.0}
	expected := []float64{-1.0, 0.0, 2.71, 3.14}
	result := BubbleSort(input)
	t.Logf("res:  %v", result)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("float64: expected %v, got %v", expected, result)
	}
}

func TestBubbleSortString(t *testing.T) {
	input := []string{"banana", "apple", "cherry"}
	expected := []string{"apple", "banana", "cherry"}
	result := BubbleSort(input)
	t.Logf("res:  %v", result)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("string: expected %v, got %v", expected, result)
	}
}
