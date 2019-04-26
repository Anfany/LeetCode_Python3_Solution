# -*- coding：utf-8 -*-
# &Author  AnFany

# 120_Triangle  三角形最小路径和


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 利用动态规划的方法
        # 从数组的倒数第二层开始，由下到上逐层更新，最终得到最小值
        #  例如： [6,5,7],
        #       [4,1,8,3]
        #  其中[6,5,7] 可更新为[6+min(1,4),5+min(1,8),7+min(8,3)]=[7,6,10],
        # 也就是每个数加上下一层的相邻的两个数中的较小值

        base_list = triangle[0]  # 对于triangle只有一行的情况
        for i in range(len(triangle) - 2, -1, -1):  # 从下到上
            # 状态转移方程
            base_list = [min(triangle[i + 1][h], triangle[i + 1][h + 1]) + triangle[i][h] for h in range(len(triangle[i]))]
            # 更新
            triangle[i] = base_list

        return base_list[0]






