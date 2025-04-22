# https://leetcode.cn/problems/insert-delete-getrandom-o1/description

import random


class RandomizedSet:

    def __init__(self):
        self.nums = []      # 变长数组可以在 O(1) 的时间内完成获取随机元素操作
        self.indices = {}   # 哈希表可以在 O(1) 的时间内完成插入和删除操作

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        idx = self.indices[val]
        self.nums[idx] = self.nums[-1]      # 把数组最后一个补充到移除元素的位置
        self.indices[self.nums[idx]] = idx  # 相应的哈希表内容也要修改
        self.nums.pop()                     # 然后把数组最后一个pop掉，即删除
        del self.indices[val]               # 同理删除哈希表相应内容
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


def main():
    obj = RandomizedSet()
    test_list = [
        # func, args
        ["insert", 7],          # true
        ["insert", 2],          # true
        ["getRandom", None],
        ["insert", 7],          # false
        ["insert", 8],          # true
        ["remove", 7],          # true
        ["remove", 10],         # false
        ["insert", 4],          # true
        ["getRandom", None],
    ]
    for func_name, args in test_list:
        try:
            func = getattr(obj, func_name)
        except:
            func = None
            print("error func name")
        if func is None:
            continue
        if args is not None:
            res = func(args)
        else:
            res = func()
        print(f"{res}")


if __name__ == '__main__':
    main()