# -*- coding：utf-8 -*-
# &Author  AnFany

# 64_Minimum_Path_Sum 最小路径和


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 利用动态规划的方法
        # 要到达索引为[r,l]的网格
        # 一是从[r,l-1]的网格向右走过来的
        # 二是从[r-1,l]的网格向下过来的
        # 令S[r,l]表示到达索引为[r,l]的网格的最短路径
        # 则动态规划的状态转移方程为S[r,l] = min(S[r-1,l], S[r,l-1]) + grid[r,l]

        m, n = len(grid), len(grid[0])  # 网格的行数和列数

        if not m:  # 行列为0
            return 0
        # 存储最短的路径的数组。只需要2行即可

        # 开始利用动态规划寻找最小路径
        for r in range(m):
            for l in range(n):
                # 对于边界之外的网格，令该网格的数为正无穷大
                if r >= 1 and l >= 1:
                    grid[r][l] = grid[r][l] + min(grid[r - 1][l], grid[r][l - 1])
                elif r >= 1:
                    grid[r][l] = grid[r][l] + grid[r - 1][l]
                elif l >= 1:
                    grid[r][l] = grid[r][l] + grid[r][l - 1]

        return grid[-1][-1]


