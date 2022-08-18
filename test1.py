

def main(a):
    result = 0
    for i in range(1, a + 1):
        fenzi = i
        fenmu = a & -a
        each = fenzi / fenmu
        result += each
    return result


if __name__ == '__main__':
    t = int(input().strip())
    for i in range(t):
        a = int(input().strip())
        result = main(a)
        print(result)