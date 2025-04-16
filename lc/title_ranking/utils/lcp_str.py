

def lcp(str1: str, str2: str) -> str:
    length = min(len(str1), len(str2))
    index = 0
    while index < length and str1[index] == str2[index]:
        index += 1
    return str1[:index]


def main():
    str1 = "flower"
    str2 = "flow"
    res = lcp(str1, str2) # "flow"
    print(res)


if __name__ == '__main__':
    main()