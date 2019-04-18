# -*- coding：utf-8 -*-
# &Author  AnFany
# 20_Valid_Parentheses 有效的括号

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:  # 空字符串是有效的
            return True
        else:
            parentheses = []  # 栈
            match_dict = {']': '[',  ')': '(', '}': '{'}  # 匹配的字典
            for i in s:
                if not parentheses:
                    parentheses.append(i)
                else:
                    if i not in match_dict:  # 说明是左括号
                        parentheses.append(i)  # 进栈
                    else:
                        if match_dict[i] == parentheses[-1]:  # 可以匹配上
                            parentheses.pop(-1) # 出栈
                        else:
                            return False  # 匹配不上，是无效的
            if not parentheses:
                return True
            else:
                return False


