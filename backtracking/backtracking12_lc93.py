
# 组合问题(没整明白)
class Solution:
    def __init__(self):
        self.result = []

    def restoreIpAddresses(self, s):
        '''
        本质切割问题使用回溯搜索法，本题只能切割三次，所以纵向递归总共四层
        因为不能重复分割，所以需要start_index来记录下一层递归分割的起始位置
        添加变量point_num来记录逗号的数量[0,3]
        '''
        self.result.clear()
        if len(s) > 12:
            return []
        self.backtracking(s, 0, 0)
        return self.result

    def backtracking(self, s, start_index, point_num):
        # Base Case
        if point_num == 3:
            if self.is_valid(s, start_index, len(s)-1):
                self.result.append(s[:])
            return
        # 单层递归逻辑
        for i in range(start_index, len(s)):
            if self.is_valid(s, start_index, i):        # [start_index, i]就是被截取的子串
                s = s[:i+1] + '.' + s[i+1:]
                self.backtracking(s, i+2, point_num+1)  # 在填入.后，下一子串起始后移2位
                s = s[:i+1] + s[i+2:]    # 回溯
            else:
                # 若当前被截取的子串大于255或者大于三位数，直接结束本层循环
                break
    
    def is_valid(self, s, start, end):
        if start > end:
            return False
        if s[start] == '0' and start != end:        # 若数字是0开头，不合法
            return False
        if not 0 <= int(s[start:end+1]) <= 255:
            return False
        return True

aaa = Solution()
bbb = aaa.restoreIpAddresses("25525511135")
print(bbb)      # ["255.255.11.135","255.255.111.35"]