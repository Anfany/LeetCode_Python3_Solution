# -*- coding：utf-8 -*-
# &Author  AnFany
# 20_Valid_Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        else:
            parentheses = []
            match_dict = {']': '[',  ')': '(', '}': '{'}
            for i in s:
                if not parentheses:
                    parentheses.append(i)
                else:
                    if i not in match_dict:
                        parentheses.append(i)
                    else:
                        if match_dict[i] == parentheses[-1]:
                            parentheses.pop(-1)
                        else:
                            return False
            if not parentheses:
                return True
            else:
                return False


