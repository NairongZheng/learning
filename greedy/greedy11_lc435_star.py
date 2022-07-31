

def eraseOverlapIntervals(intervals):
    """
        无重叠区间
        给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
        注意: 可以认为区间的终点总是大于它的起点。 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

        思路：还是看看解答
        按照右边界排序，从左向右记录非交叉区间的个数。最后用区间总数减去非交叉区间的个数就是需要移除的区间个数了。
        此时问题就是要求非交叉区间的最大个数。

        总结如下难点：
        难点一：一看题就有感觉需要排序，但究竟怎么排序，按左边界排还是右边界排。
        难点二：排完序之后如何遍历，如果没有分析好遍历顺序，那么排序就没有意义了。
        难点三：直接求重复的区间是复杂的，转而求最大非重复区间个数。
        难点四：求最大非重复区间个数时，需要一个分割点来做标记。
    """
    # 按照左区间排序
    intervals.sort(key=lambda x:x[0])       # 左区间排序
    count = 1                   # 记录非交叉区间个数
    end = intervals[-1][0]      # 记录区间分割点
    for i in range(len(intervals) - 2, -1, -1):
        if end >= intervals[i][1]:
            count += 1
            end = intervals[i][0]
    return len(intervals) - count

    # # 按照右区间排序
    # intervals.sort(key=lambda x:x[1])     # 右区间排序
    # count = 1           # 记录非交叉区间的个数
    # end = intervals[0][1]   # 记录区间分割点
    # for i in range(1, len(intervals)):    # 从左往右遍历
    #     if end <= intervals[i][0]:
    #         count += 1
    #         end = intervals[i][1]
    # return len(intervals) - count

aaa = eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
print(aaa)          # 1