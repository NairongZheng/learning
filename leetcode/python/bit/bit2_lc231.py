

def isPowerOfTwo(n):
    """
        2的幂
        给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
    """

    # 如果是2的幂，那么二进制表示1的个数就只有一个
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
    if count == 1:
        return True
    else:
        return False

aaa = isPowerOfTwo(3)
print(aaa)