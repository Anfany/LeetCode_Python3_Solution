# -*- coding：utf-8 -*-
# &Author  AnFany

# 14_Longest_Common_Prefix  最长公共前缀


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 首先比较所有字符串索引为0的位置上的字母，然后判断索引为1的位置上的字母，依次判断
        # 直到出现不一样的字母或者出现了溢出边界的状况，就停止

        length = len(strs)
        if length == 1:  # 1个字符串的最长公共前缀就是其本身
            return strs[0]
        elif not length:
            return ''

        start_index = 0

        while 1:
            new_str = ''
            for s in strs:
                if not new_str:
                    try:
                        new_str = s[start_index]
                    except IndexError:  # 溢出边界
                        return s[:start_index]
                else:
                    try:
                        if new_str != s[start_index]:  # 出现不一样的字母
                            return s[:start_index]
                    except IndexError:  # 溢出边界
                        return s[:start_index]
            start_index += 1  # 索引加1
