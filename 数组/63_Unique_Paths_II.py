# -*- coding：utf-8 -*-
# &Author  AnFany

# 63_Unique_Paths_II 不同路径II


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 利用动态规划
        # 要到达索引为[r,l]的网格，有两种方式
        # 一是从[r,l-1]的网格向右走过来的
        # 二是从[r-1,l]的网格向下过来的
        # 令S[r,l]表示到达索引为[r,l]的网格的不同路径的个数
        # 则动态规划的方程为S[r,l] = S[r-1,l]+S[r,l-1],如果网格[r,l],[r-1,l],[r,l-1]均不包含障碍物
        # 对于包含障碍物的网格S[r,l] = 0

        # 获取列，行
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        #  行列网格数有一个为0，就返回0
        if not m or not n:
            return 0
        # 行列网格数有一个为1，没有障碍物就返回1，有障碍物就返回0
        elif m == 1 or n == 1:
            if 1 in obstacleGrid[0] or [1] in obstacleGrid:
                return 0
            return 1

        # 定义二维数组，防止溢出边界，数组行、列均加1
        s = [[0 for i in range(m + 1)] for j in range(n + 1)]

        # 给定的网格数组也要添加行和列
        obstacleGrid.insert(0, obstacleGrid[0])  # 添加行
        for index, value in enumerate(obstacleGrid):
            copy_value = value.copy()
            copy_value = [copy_value[0]] + copy_value
            obstacleGrid[index] = copy_value

        # 动态规划的初始状态
        s[0][1] = 1

        # 开始遍历
        for r in range(1, n + 1):
            for l in range(1, m + 1):
                if not obstacleGrid[r][l]:
                    #  在计算时判断网格是否有障碍物
                    s[r][l] = s[r - 1][l] * (not obstacleGrid[r - 1][l]) \
                              + s[r][l - 1] * (not obstacleGrid[r][l - 1])
                else:
                    s[r][l] = 0
                print(s)

        return s[-1][-1]

