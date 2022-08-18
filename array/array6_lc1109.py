

def corpFlightBookings(bookings, n):
    """
        航班预定统计
        这里有 n 个航班，它们分别从 1 到 n 进行编号。
        有一份航班预订表bookings
        表中第i条预订记录bookings[i] = [firsti, lasti, seatsi]意味着在从firsti到lasti（包含 firsti 和 lasti ）的每个航班上预订了seatsi个座位。
        请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。
    """
    diff = [0 for _ in range(n)]        # 差分数组，记录每次预定之后的变化，用于反推出结果数组
    for book in bookings:
        i, j, val = book
        diff[i - 1] += val
        if j < len(diff):
            diff[j] -= val
    
    # 开始从差分数组反推
    result = [0 for i in range(len(diff))]
    result[0] = diff[0]
    for i in range(1, len(diff)):
        result[i] = (diff[i] + result[i - 1])
    return result

aaa = corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5)
print(aaa)      # [10, 55, 45, 25, 25]