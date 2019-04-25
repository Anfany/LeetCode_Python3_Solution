# -*- coding：utf-8 -*-
# &Author  AnFany

# 13_Roman_to_Integer  罗马数字转整数


class Solution:
    def __init__(self):
        # 字符z是自定义的，编程便利性
        self.roman_integer_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'z': 0}

    def romanToInt(self, s: str) -> int:
        # 只要该字符对应的正数大于前一个字符对应的整数，就需要减去前一个数值
        first_roman = s[0]  # 第一个字符

        if len(s) == 1:
            return self.roman_integer_dict[first_roman]

        integer = 0  # 最终的整数

        poss_sign = 1  # 判断是否有前一个字符的标识

        s += 'z'  # 在字符串最后添加自定义的新字符，编程便利性

        for i in s[1:]:
            if not poss_sign:  # 前一个字符不存在, 则当前字符设定为前一个字符
                first_roman = i
                poss_sign = 1
            else:
                current_integer = self.roman_integer_dict[i]  # 当前数字
                forward_integer = self.roman_integer_dict[first_roman]  # 前一个数字
                if current_integer <= forward_integer:
                    integer += forward_integer  # 则加上前一个数字
                    first_roman = i  # 当前字符定义为下一个字符
                else:  # 此时就是特殊情况，需要进行减法运算
                    integer += current_integer - forward_integer  # 则加上两者的查
                    poss_sign = 0  # 此时前一个字符的标识设置为0
        return integer

