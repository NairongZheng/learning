

def carPooling(trips, capacity):
    """
        拼车
        车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）
        给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有 numPassengersi 乘客，
        接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。
        当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。
        0 <= fromi < toi <= 1000
    """
    diff = [0 for _ in range(1001)]     # 构造一个差分数组，题目说了范围的，或者可以每次遍历一下trips看看这个样例最远的车站在哪里，再去构建
    for trip in trips:
        val, i, j = trip
        diff[i] += val
        if j < len(diff):               # 注意题目说的，从to就会下车，所以跟之前的题目不一样，不是在j+1的地方减，而实在j的地方
            diff[j] -= val
    result = [0 for _ in range(len(diff))]      # 从差分数组逆推结果数组
    result[0] = diff[0]
    for i in range(1, len(result)):
        result[i] = diff[i] + result[i - 1]
        if result[i] > capacity:
            return False
    if result[0] > capacity:        # 判断写在循环里，但是第一个没有进循环，所以要再判断一次
        return False
    return True

aaa = carPooling([[2,1,5],[3,3,7]], 4)
print(aaa)      # False