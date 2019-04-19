# -*- coding：utf-8 -*-
# &Author  AnFany
# 3_Longest_Substring_Without_Repeating_Characters  无重复字符的最长子串


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 新字符串的起始点
        start = 0
        # 存储最大长度
        max_length = 0
        # 字典形式存储已经遍历过的字符
        str_dict = {}
        # 开始遍历
        for j in range(len(s)):
            if s[j] in str_dict:
                # 之前出现过， 此时出现了重复的字符
                # 判断这个字符的位置是不是在start的后面，如果在前面是没有影响的
                if start <= str_dict[s[j]]:
                    # 此时需要计算无重复字符的子串的长度
                    max_length = max(max_length, j - start)
                    # 需要更新起始点
                    start = str_dict[s[j]] + 1
            # 更新这个字符出现的位置
            str_dict[s[j]] = j

        return max(max_length, len(s) - start)

