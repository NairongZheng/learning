package test

import (
	"fmt"
	"testing"

	"github.com/nairongzheng/simple_go/pkg/utils"
)

func TestAdd(t *testing.T) {
	result := utils.Add(1, 2)
	fmt.Println("Result of Add(1, 2):", result) // 打印结果
	t.Logf("Result of Add(1, 2) = %d", result)  // go test -v 中打印结果
	if result != 3 {
		t.Errorf("Expected 3, got %d", result)
	}
}
