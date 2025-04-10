
def count_bits_1(n):
    """
        计算一个数的二进制中, 1的数量
        方法一：朴实无华挨个计算1的数量，最多就是循环n的二进制位数，32位。
    """
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n >>= 1
    return count


def count_bits_2(n):
    """
        计算一个数的二进制中, 1的数量
        方法二：这种方法，只循环n的二进制中1的个数次，比方法一高效的多
    """
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count

n = 12      # 12的二进制表示是1100

aaa = count_bits_1(n)
print(aaa)
bbb = count_bits_2(n)
print(bbb)