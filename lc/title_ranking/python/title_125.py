# https://leetcode.cn/problems/valid-palindrome/description


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
            elif not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
        return True


def main():
    test_list = [
        "A man, a plan, a canal: Panama",  # true
        "race a car",  # false
    ]
    for s in test_list:
        res = Solution().isPalindrome(s)
        print(f"{res}")


if __name__ == "__main__":
    main()
