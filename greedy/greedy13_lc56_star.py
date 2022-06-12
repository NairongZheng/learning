

def merge(intervals):
    """
        合并区间
        给出一个区间的集合，请合并所有重叠的区间。
    """
    # 右边界排序
    intervals.sort(key=lambda x:x[1])
    result = []
    result.append(intervals[-1])
    for i in range(len(intervals) - 2, -1, -1):
        last = result[-1]
        if last[0] <= intervals[i][1]:
            result[-1] = [min(last[0], intervals[i][0]), last[1]]
        else:
            result.append(intervals[i])
    return result

    # # 左边界排序
    # intervals.sort(key=lambda x:x[0])
    # result = []
    # result.append(intervals[0])
    # for i in range(1, len(intervals)):
    #     last = result[-1]
    #     if last[-1] >= intervals[i][0]:
    #         result[-1] = [last[0], max(last[1], intervals[i][1])]
    #     else:
    #         result.append(intervals[i])
    # return result

aaa = merge([[1,3],[2,6],[8,10],[15,18]])
print(aaa)