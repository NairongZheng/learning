

def nextGreatestLetter(letters, target):
    """
        寻找比目标字母大的最小字母
    """
    if ord(letters[-1]) <= ord(target):
        return letters[0]

    left = 0
    right = len(letters) - 1
    while left < right:
        mid = (left + right) // 2
        if ord(letters[mid]) <= ord(target):    # 这边用<,>,<=,>=要自己好好想想(这边是难点, 要根据具体题目来判断)
            left = mid + 1
        else:
            right = mid
    return letters[left]

aaa = nextGreatestLetter(['c', 'f', 'j'], 'a')
print(aaa)