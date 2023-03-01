

def reconstructQueue(people):
    """
        根据身高重建队列
        假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。
        每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
        请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，
        其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。
    """
    # 先按照h维度的身高顺序从高到低排序。确定第一个维度
    # lambda返回的是一个元组：当-x[0](维度h）相同时，再根据x[1]（维度k）从小到大排序
    people.sort(key=lambda x:(-x[0], x[1]))
    que = []

    # 根据每个元素的第二个维度k，贪心算法，进行插入
    # people已经排序过了：同一高度时k值小的排前面。
    for p in people:
        que.insert(p[1], p)
    return que

aaa = reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
print(aaa)      # [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]