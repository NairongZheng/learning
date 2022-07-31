def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort(key=lambda x: (x[0], x[1]))
    stack = [intervals[-1]]
    for i in range(len(intervals) -2, -1, -1):
        if stack[-1][0] <= intervals[i][1]:
            cur = stack.pop()
            stack.append([intervals[i][0], cur[1]])
        else:
            stack.append(intervals[i])
    return stack

aaa = merge([[1,4],[2,3]])