

def findContentChildren(g, s):
    """
        分发饼干
        示例1: 输入g = [1,2,3], s = [1,1]; 输出1
        解释你有三个孩子和两块小饼干, 3个孩子的胃口值分别是:1,2,3. 虽然你有两块小饼干, 由于他们的尺寸都是1, 你只能让胃口值是1的孩子满足

        思路: 为了满足更多的小孩, 就不要造成饼干尺寸的浪费
        大尺寸的饼干既可以满足胃口大的孩子也可以满足胃口小的孩子, 那么就应该优先满足胃口大的
        这里的局部最优就是大饼干喂给胃口大的, 充分利用饼干尺寸喂饱一个, 全局最优就是喂饱尽可能多的小孩
        可以尝试使用贪心策略, 先将饼干数组和小孩数组排序
        然后从后向前遍历小孩数组, 用大饼干优先满足胃口大的, 并统计满足小孩数量
    """
    # # 优先考虑饼干
    # g.sort()
    # s.sort()
    # result = 0
    # for i in range(len(s)):
    #     if result < len(g) and s[i] >= g[result]:       # 小饼干先喂饱小胃口
    #         result += 1
    # return result

    # 优先考虑胃口
    g.sort()
    s.sort()
    start = len(s) - 1
    result = 0
    for i in range(len(g) - 1, -1, -1):              # 先喂饱大胃口
        if start >= 0 and g[i] <= s[start]:
            start -= 1
            result += 1
    return result

aaa = findContentChildren([1,2,3],[1,1])
print(aaa)