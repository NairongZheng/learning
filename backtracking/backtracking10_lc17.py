
# 组合问题(多个集合取组合)
def letterCombinations(digits):
    """
        电话号码的字母组合
        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
    """
    letter_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
                        '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    path = []
    result = []

    def backtracking(digits, index):
        if index == len(digits):
            result.append(''.join(path))
            return
        letters = letter_map[digits[index]]
        for letter in letters:
            path.append(letter)
            backtracking(digits, index + 1)
            path.pop()

    if not digits:
        return []
    backtracking(digits, 0)
    return result

aaa = letterCombinations('23')
print(aaa)      # ["ad","ae","af","bd","be","bf","cd","ce","cf"]