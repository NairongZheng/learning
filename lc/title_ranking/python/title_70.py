# https://leetcode.cn/problems/climbing-stairs/description


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


def main():
    test_list = [
        2,  # 2
        3,  # 3
        4,  # 5
    ]
    for n in test_list:
        res = Solution().climbStairs(n)
        print(f"{res}")


if __name__ == "__main__":
    main()
