package problems

import "lc_go/utils"

func Rotate(nums []int, k int) {
	n := len(nums)
	if n == 0 {
		return
	}

	k %= n
	utils.Reverse(nums)     // 使用utils包中的Reverse函数
	utils.Reverse(nums[:k]) // 反转前k个元素
	utils.Reverse(nums[k:]) // 反转剩余的部分
}
