package utils

import (
	"os"
)

func Add(a, b int) int {
	return a + b
}

func ReadJSONFile(filePath string) ([]byte, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return nil, err
	}
	return data, nil
}
