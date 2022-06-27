"""
    quthor:damonzheng
    function:快速排序
    date:2022.4.23
    可参考：https://www.bilibili.com/video/BV1K44y1k79z/
"""

def quick_sort(nums, head, tail):
    """
        好好理解这个
    """
    if head >= tail:        # 迭代退出的条件
        return nums         # 递归终止条件：如果要排序的列表只有一个元素，或者为空，都不用操作，直接返回就可以
    
    pivot = nums[head]     # 选择第一个元素作为基准元素
    left = head
    right = tail

    while left != right:
        while left < right and nums[right] >= pivot:    # 右值大于pivot，右指针左移
            right -= 1
        nums[left] = nums[right]                      # 否则，右值比pivot小，应该放在左边，就直接拿过去填坑（pivot取出来不是有一个坑嘛）

        while left < right and nums[left] <= pivot:     # 左值小于pivot，左指针右移
            left += 1
        nums[right] = nums[left]                      # 否则，左值比pivot大，应该放在右边，拿过去填刚刚那个坑

    nums[left] = pivot     # 当left==right时，循环结束，剩下的这个坑就是pivot的位置。左边都比他小，右边都比他大

    quick_sort(nums, head, left - 1)
    quick_sort(nums, left + 1, tail)

    return nums     # 这句是可以不用的

def quick_sort2(data):
    """
        缺点：要申请新的空间、原数组会有一个被remove
        所以这个虽然理解简单但是不推荐
    """
    if len(data) >= 2:  # 递归入口及出口
        mid = data[len(data)//2]  # 选取基准值，也可以选取第一个或最后一个元素
        left, right = [], []  # 定义基准值左右两侧的列表
        data.remove(mid)  # 从原始数组中移除基准值
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort2(left) + [mid] + quick_sort2(right)
    else:
        return data

def quick_sort3(nums, startIdx, endIdx):    # nums：要排序的列表，startIdx：要排序的起始位置，endIdx：要排序的终止位置
    """
        其实跟quick_sort是一样的
    """
    # 递归终止条件：如果要排序的列表只有一个元素，或者为空，都不用操作，直接返回就可以
    if startIdx >= endIdx:
        return
    
    pivotIdx = startIdx     # 选取一个基准值，直接用第一个就好
    left = startIdx + 1     # 左指针
    right = endIdx          # 右指针

    while left <= right:    # 循环终止的条件是left > right的时候

        if nums[left] > nums[pivotIdx] and nums[right] < nums[pivotIdx]:    # 如果左值大于基准值并且右值小于基准值，那么就把左右值对换
            nums[left], nums[right] = nums[right], nums[left]               # （因为要保证左小于基准，右大于基准）
        
        if nums[left] <= nums[pivotIdx]:        # 如果左值小于等于基准值，就直接把左指针向右边移动继续判断
            left += 1
        
        if nums[right] >= nums[pivotIdx]:       # 如果右值大于等于基准值，就直接把右指针向左边移动继续判断
            right -= 1
        
    nums[pivotIdx], nums[right] = nums[right], nums[pivotIdx]       # left > right时循环结束，把right跟基准值对换

    quick_sort3(nums, startIdx, right - 1)
    quick_sort3(nums, right + 1, endIdx)
    return nums


# sorted_list1 = quick_sort([3, 2, 1, 9, 6, 5, 4], 0, 6)
sorted_list1 = quick_sort([5,2,3,1,4], 0, 4)
print(sorted_list1)

# sorted_list2 = quick_sort2([3, 2, 1, 9, 6, 5, 4])
# print(sorted_list2)

# sorted_list3 = quick_sort3([1,2,3,2,5,6], 0, 5)
# print(sorted_list3)

pass