# -*- coding：utf-8 -*-
# &Author  AnFany

# 7_Reverse_Integer 整数反转



class Solution:

    def __init__(self):
        self.max_num = 2 ** 31 - 1
        self.min_num = - 2 ** 31

    def reverse(self, x: int) -> int:
        #  反转不利用字符串的反转，利用%不断获取最后一位数字
        #  分负，非负2种情况
        if x < 0:
            new_num = '-'  # 负数情况
            x = -x
        elif x == 0:   # 等于0的情况
            new_num = 0
        else:
            new_num = ''
        # 开始反转
        while x != 0:
            new_num += str(x % 10)
            x //= 10

        # 判断是否在区间内
        if self.min_num <= int(new_num) <= self.max_num:
            return int(new_num)
        else:
            return 0










