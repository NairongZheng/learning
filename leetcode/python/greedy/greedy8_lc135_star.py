

def candy(ratings):
    """
        分发糖果
        老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
        你需要按照以下要求，帮助老师给这些孩子分发糖果：
            每个孩子至少分配到 1 个糖果。
            相邻的孩子中，评分高的孩子必须获得更多的糖果。
        那么这样下来，老师至少需要准备多少颗糖果呢？

        这道题目一定是要确定一边之后，再确定另一边，例如比较每一个孩子的左边，然后再比较右边，如果两边一起考虑一定会顾此失彼。
        先确定右边评分大于左边的情况（也就是从前向后遍历）; 再确定左孩子大于右孩子的情况（从后向前遍历）
        遍历顺序这里有同学可能会有疑问，为什么不能从前向后遍历呢？
        因为如果从前向后遍历，根据 ratings[i + 1] 来确定 ratings[i] 对应的糖果，那么每次都不能利用上前一次的比较结果了。
    """
    candyVec = [1] * len(ratings)
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            candyVec[i] = candyVec[i - 1] + 1
    for j in range(len(ratings) - 2, -1, -1):
        if ratings[j] > ratings[j + 1]:
            candyVec[j] = max(candyVec[j], candyVec[j + 1] + 1)         # 这个也要注意啦，要取大的
    return sum(candyVec)

aaa = candy([1,0,2])
print(aaa)