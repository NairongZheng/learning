import re


def re_match_1():
    """
    1. ^：匹配字符串的开头。确保匹配从字符串的第一个字符开始。
    2. [a-zA-Z0-9_.+-]+：最后一个+表示前面括号中的字符集至少匹配一次，且可以匹配多次。
    3. @：匹配 "@" 字符，这是邮箱地址中分隔用户名和域名的符号。
    4. [a-zA-Z0-9-]+：类似2
    5. \.：匹配一个点号 .。因为点号在正则表达式中是一个特殊字符，表示任意字符，所以在这里需要使用反斜杠 \ 进行转义，表示匹配实际的点号字符。
    6. [a-zA-Z0-9-.]+：类似2
    7. $：匹配字符串的结尾。确保整个字符串从头到尾完全匹配该正则表达式，即没有多余的字符。
    """
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    email_list = [
        "example@domain.com", # 格式正确
        "user.name+test@example.co.uk", # 格式正确
        "example@domain", # 缺少顶级域名部分
        "@domain.com", # 缺少用户名部分
    ]
    for email in email_list:
        re_result = re.match(email_pattern, email)
        if re_result:
            print(f"{re_result.group()}邮箱格式正确") # re_result.group()返回匹配到的内容
        else:
            print(f"{email}邮箱格式不正确")


def re_match_2():
    # 分组 "bc" 或者多个 "b"
    pattern = r"ab(c|b+)d"
    test_str_list = ["abcd", "abbbbd", "abd", "abbbbcd"] # 匹配、匹配、不匹配、不匹配
    for test_str in test_str_list:
        re_result = re.match(pattern, test_str)
        if re_result:
            print(f"{re_result.group()}匹配")
        else:
            print(f"{test_str}不匹配")


def re_search():
    text = "我的生日是1995-06-15。"
    # 捕获年份、月份和日期
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', text)
    if match:
        # 打印捕获组中的内容
        print(f"年份: {match.group(1)}")
        print(f"月份: {match.group(2)}")
        print(f"日期: {match.group(3)}")


def re_findall():
    """
    \.[a-zA-Z]{2,} 匹配域名后缀（如 .com、.org 等，至少2个字母）。
    """
    text = "请联系support@example.com或admin@company.com了解更多信息。"
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    if emails:
        print(f"找到以下邮箱地址: {emails}")
    else:
        print("未找到任何邮箱地址")


def re_sub():
    """
    r'\3/\2/\1' 表示替换顺序，将第三个捕获组（日期）放在最前，第二个捕获组（月份）在中间，第一个捕获组（年份）最后。
    """
    text = "今天是2024-10-22，我的生日是1995-06-15。"
    # 将日期格式从 YYYY-MM-DD 替换为 DD/MM/YYYY
    new_text = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', text)
    print(f"替换后的文本: {new_text}")


def re_split():
    text = "apple, orange; banana grape; kiwi, mango"
    # 使用正则表达式分割字符串，匹配逗号、分号和空格
    pattern = r'[;, ]+'
    fruits = re.split(pattern, text)
    # 输出分割后的结果
    print(fruits)


def main():
    re_match_1()
    re_match_2()
    re_search()
    re_findall()
    re_sub()
    re_split()


if __name__ == "__main__":
    main()
