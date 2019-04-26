# -*- coding：utf-8 -*-
# &Author  AnFany

# 6_ZigZag_Conversion  Z字形变换


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 行数等于1，原样返回，等于0，返回空字符串
        if numRows == 1:
            return s
        elif not numRows:
            return ''

        # 按照得到的规律进行编程
        trans_str = ''
        # 字符串长度
        length = len(s)

        for i in range(numRows):
            start_index = i
            index_gap = [2 * (numRows - 1) - 2 * i, 2 * i]
            gap = 0  # 控制选取间隔的索引
            while start_index < length:
                if index_gap[gap]:  # 对于前一个间隔为0的，需要判断，不能添加同一个字符。
                    trans_str += s[start_index]
                start_index += index_gap[gap]
                gap = not gap  # 间隔进行循环
        return trans_str

