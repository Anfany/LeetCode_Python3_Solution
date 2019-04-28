# -*- coding：utf-8 -*-
# &Author  AnFany

# 10_Regular_Expression_Matching  正则表达式匹配



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 利用动态规划的方法，动态规划四要素，如何表示状态，初始的状态是什么，以及状态之间转移的方程， 什么时候结束
        # 状态的表示：dp[i][j]表示s[:i]和p[:j]是否可匹配，其中i，j就可看作状态，dp[i][j]=1，说明可以匹配，p[i][j]=0，说明不可以匹配
        # 初始的状态：dp[0][0]=1，空字符串是可以匹配的
        # 状态转移方程：
        # 如果s[i] == p[j] or p[j] == '.'，则有dp[i][j] = dp[i-1][j-1]。
        # 如果p[j] == '*':  # 此时需要分情况讨论,
        #      (1)：如果p[j - 1] == s[i] or p[j - 1]== '.'，则有
        #                dp[i][j] = 1，只要dp[i - 1][j]，dp[i][j - 1]，dp[i][j - 2]有一个为1。
        #                dp[i][j] = 0，只要dp[i - 1][j]，dp[i][j - 1]，dp[i][j - 2]全为0。
        #                其中dp[i][j - 2]=1，说明*号匹配了0个，dp[i][j - 2]=1，说明*号只需要匹配一个
        #                dp[i - 1][j]=1，说明*号匹配了多个
        #      (2)：如果p[j-1] != s[i]，则有
        #               dp[i][j] = dp[i][j-2]  #  说明这个*号匹配了0个p[j-1]这个字母，因此这个状态值等于j往前推2个的值
        # 结束：字符串的对应关系遍历完毕

        len_s, len_p = len(s), len(p)

        dp = [[0 for _ in range(len_p + 1)] for _ in range(len_s + 1)]  # 行数为字符串s的长度，列数为字符串p的长度

        dp[0][0] = 1  # 初始条件，s，p进行匹配的字符串长度均为0
        # 首先确定匹配s中第一个字符的情况
        for i in range(1, len_p + 1):
            if p[i - 1] == '*' and dp[0][i - 2]:
                dp[0][i] = 1

        for i in range(1, len_s + 1):  # 字符串p的长度
            for j in range(1, len_p + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':  # 因为这里的i,j表示长度，因此索引需要减去1
                    dp[i][j] = dp[i-1][j-1]
                # 因为*会是第一个出现，因此j肯定不小于2，所以不会溢出
                elif p[j - 1] == '*':
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        if dp[i][j - 1] or dp[i][j - 2] or dp[i-1][j]:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = 0
                    elif p[j - 2] != s[i - 1]:
                        dp[i][j] = dp[i][j - 2]

        return 1 == dp[-1][-1]

