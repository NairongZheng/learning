

def totalFruit(tree):
    """
        水果成篮
        抽象出来就是找一个窗口, 这个窗口里面的值只能有两种(如1,2), 但是可以重复, 要找到最大的
    """
    start = 0
    max_len = float('-inf')
    adict = {}
    for end in range(len(tree)):
        # end是for循环自动更新的, 所以只要考虑什么时候更新start

        # 创建一个字典来记录这个窗口里面的东西及其个数
        if tree[end] not in adict:
            adict[tree[end]] = 1
        else:
            adict[tree[end]] += 1

        while len(adict) > 2:
            adict[tree[start]] -= 1
            if adict[tree[start]] == 0:     # 这个还是关键的
                del adict[tree[start]]
            start += 1
        max_len = max(max_len, end - start + 1)
    if max_len == float('-inf'):
        return 0
    else:
        return max_len

aaa = totalFruit([0, 1, 2, 2])
print(aaa)