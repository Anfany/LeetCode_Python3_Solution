# -*- coding：utf-8 -*-
# &Author  AnFany

# 62_Unique_Paths 不同路径


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 利用动态规划
        # 要到达索引为[r,l]的网格，有两种方式
        # 一是从[r,l-1]的网格向右走过来的
        # 二是从[r-1,l]的网格向下过来的
        # 令S[r,l]表示到达索引为[r,l]的网格的不同路径的个数
        # 则动态规划的方程为S[r,l] = S[r-1,l]+S[r,l-1]

        #  行列网格数有一个为0，就返回0
        if not m or not n:
            return 0
        # 行列网格数有一个为1，就返回1
        elif m == 1 or n == 1:
            return 1

        # 定义二维数组，防止溢出边界，数组行 列均加1
        s = [[0 for i in range(m + 1)] for j in range(n + 1)]

        # 动态规划的初始状态
        s[0][1] = 1

        # 开始遍历
        for r in range(1, n + 1):
            for l in range(1, m + 1):
                s[r][l] = s[r - 1][l] + s[r][l - 1]

        return s[-1][-1]






