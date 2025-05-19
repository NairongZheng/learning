# https://leetcode.cn/problems/text-justification/description


from typing import List


class Solution:
    def split_worlds(self, words: List[str], maxWidth: int):
        """先将每行有几个单词分好"""
        eachMaxWidth = maxWidth
        rowNum = 0
        res_list = [[]]
        for each_world in words:
            if len(each_world) == eachMaxWidth:  # 最后一个单词不用空格
                eachMaxWidth = eachMaxWidth - len(each_world)
            elif len(each_world) + 1 <= eachMaxWidth:  # 其他每个单词都需要至少一个空格
                eachMaxWidth = eachMaxWidth - len(each_world) - 1
            else:  # 不够空格就换行咯
                eachMaxWidth = maxWidth - len(each_world) - 1
                rowNum += 1
                res_list.append([])
            res_list[rowNum].append(each_world)
        return res_list

    def postprocess(self, res_list, maxWidth):
        """再处理每个单词间要加几个空格"""
        res = []  # 存放结果
        for i, each_list in enumerate(res_list):
            each_row_str = ""
            if i != len(res_list) - 1:
                each_row_world_num = 0  # 每行的单词个数
                each_row_world_len = 0  # 每行总的字母个数
                for each_world in each_list:
                    each_row_world_num += 1
                    each_row_world_len += len(each_world)
                blank_num = maxWidth - each_row_world_len  # 每行总的空格个数
                avg_blank_num = (
                    blank_num // (each_row_world_num - 1)
                    if each_row_world_num - 1 != 0
                    else blank_num
                )  # 每个间隔的空格数
                add_blank_num = (
                    blank_num % (each_row_world_num - 1)
                    if each_row_world_num - 1 != 0
                    else 0
                )  # 需要额外+1的空格数
                for each_world in each_list:
                    if add_blank_num != 0:
                        each_row_str += each_world + " " * (avg_blank_num + 1)
                        add_blank_num -= 1
                    else:
                        each_row_str += each_world + " " * (avg_blank_num)
            else:
                for each_world in each_list:
                    each_row_str += each_world + " "
                each_row_str += " " * maxWidth
            res.append(each_row_str[:maxWidth])
        return res

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res_list = self.split_worlds(words, maxWidth)
        res = self.postprocess(res_list, maxWidth)
        return res


def main():
    test_list = [
        [["This", "is", "an", "example", "of", "text", "justification."], 16],
        [["What", "must", "be", "acknowledgment", "shall", "be"], 16],
        [[ "Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20],
    ]
    for words, maxWidth in test_list:
        res = Solution().fullJustify(words, maxWidth)
        print(f"{res}")


if __name__ == "__main__":
    main()
