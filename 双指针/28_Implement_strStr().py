# -*- coding：utf-8 -*-
# &Author  AnFany

# 28_Implement_strStr()  实现strStr()


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # needle为空，返回0
        if not needle:
            return 0
        # haystack为空，返回-1
        if not haystack:
            return -1

        length_needle = len(needle)

        length_haystack = len(haystack)

        for h in range(length_haystack - length_needle + 1):
            if haystack[h] == needle[0]:  # 如果与needle的首字母相同
                if haystack[h: (h + length_needle)] == needle:  # 则开始判断字符串是否相等
                    return h
        return -1


