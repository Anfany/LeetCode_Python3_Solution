# -*- coding：utf-8 -*-
# &Author  AnFany

# 38_Count_and_Say 报数


class Solution:
    def countAndSay(self, n: int) -> str:
        start_num = 1  # 初始的数
        start_str = '1'  # 初始报数
        while start_num < n:
            new_str = ''
            forward_str = ''  # 前一个字符，判断是不是连续的字符，用于计数
            str_count = 1
            for i in range(len(start_str)):
                if forward_str:
                    if start_str[i] != forward_str:
                        new_str += '%s%s' % (str_count, forward_str)  # 开始报数，个数加上数值
                        str_count = 1
                        forward_str = start_str[i]
                    else:
                        str_count += 1
                else:
                    forward_str = start_str[i]
            new_str += '%s%s' % (str_count, start_str[-1])  # 最后数值的报数

            start_str = new_str  # 这一轮报出的数就是下一轮要报的数

            start_num += 1
        return start_str







