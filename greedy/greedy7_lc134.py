

def canCompleteCircuit(gas, cost):
    """
        加油站
        在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
        你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
        如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
        说明：如果题目有解，该答案即为唯一答案。
    """
    if sum(gas) - sum(cost) < 0:    # 如果gas的总和小于cost总和，那么无论从哪里出发，一定是跑不了一圈的!!!!!!!!!!!!!!
        return -1
    start = 0
    curSum = 0
    for i in range(len(gas)):
        curSum += gas[i] - cost[i]
        if curSum < 0:          # 当前累积rest[i]和curSum一旦小于0
            start = i + 1       # 起始位置更新为i+1
            curSum = 0
    return start

aaa = canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
print(aaa)          # 3