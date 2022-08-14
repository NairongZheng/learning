

def topKFrequent(nums, k):
    """
        前 K 个高频元素
        给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
        题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
        进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
    """
        
    # 堆, 时间复杂度为O(nlogk)
    from collections import Counter
    import heapq
    adict = Counter(nums)
    smallheap = []
    for num, count in adict.items():
        if len(smallheap) < k:
            heapq.heappush(smallheap, (count, num))
        elif count > smallheap[0][0]:
            heapq.heappop(smallheap)
            heapq.heappush(smallheap, (count, num))
        else:
            continue
    return [x[1] for x in smallheap]

    # # 用排序的方法, 时间复杂度为O(nlogn), 不满足题目要求
    # from collections import Counter
    # adict = Counter(nums)
    # adict = sorted(adict.items(), key=lambda x: x[1], reverse=True)
    # result = []
    # for i in range(k):
    #     result.append(adict[i][0])
    # return result

aaa = topKFrequent([1,1,1,2,2,3], 2)
print(aaa)      # [1, 2]