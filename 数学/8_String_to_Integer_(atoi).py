# -*- coding：utf-8 -*-
# &Author  AnFany

# 8_String_to_Integer_(atoi) 字符串转换整数(atoi)


class Solution:
    def __init__(self):
        self.max_num = 2 ** 31 - 1
        self.min_num = - 2 ** 31

    def myAtoi(self, str: str) -> int:
        # 获取的表示整数的字符串
        new_integer_str = ''

        str = str.lstrip()  # 首先替换左边的所有空格

        for s in str:
            if s == '-' or s == '+':
                if not new_integer_str:
                    new_integer_str += s
                else:
                    break
            else:
                try:
                    int(s)
                    new_integer_str += s

                except ValueError:
                    break


        # 开始判断
        try:
            if self.min_num > int(new_integer_str):
                return self.min_num
            elif self.max_num < int(new_integer_str):
                return self.max_num
            else:
                return int(new_integer_str)
        except ValueError:  # 针对new_integer_str='-' or '+'
            return 0



