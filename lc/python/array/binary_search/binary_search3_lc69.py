

def mySart(x):
    """
        x的平方根
    """
    left = 0
    right = x // 2 + 1
    while left < right:
        mid = (left + right + 1) // 2
        if mid ** 2 > x:
            right = mid - 1
        else:
            left = mid
    print('x的平方根是{}'.format(left))

aaa = mySart(4)