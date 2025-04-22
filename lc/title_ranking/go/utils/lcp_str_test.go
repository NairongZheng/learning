package utils

import (
	"testing"
)

func TestLcp(t *testing.T) {
	tests := []struct {
		input  []string
		expect string
	}{
		{
			input:  []string{"flower", "flow"},
			expect: "flow",
		},
		{
			input:  []string{"dog", "racecar"},
			expect: "",
		},
	}

	for _, tt := range tests {
		str1 := tt.input[0]
		str2 := tt.input[1]
		res := Lcp(str1, str2)
		t.Logf("res:  %v", res)
		if res != tt.expect {
			t.Errorf("Expected %s, but got %s", tt.expect, res)
		}
	}
}
