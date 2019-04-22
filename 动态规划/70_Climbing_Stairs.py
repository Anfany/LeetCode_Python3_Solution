# -*- coding：utf-8 -*-
# &Author  AnFany

# 70_Climbing_Stairs 爬楼梯


class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划的思想
        # 爬到n阶有2种情况：一是从n-2阶爬了2阶来到的，二是从n-1阶爬了一阶来到的
        # 令F(n)表示到达n阶的不同的方法个数，因此F(n) = F(n-1) + F(n-2)
        f1, f2 = 1, 2
        if n == 1:
            return f1
        stsirs = 2
        while stsirs < n:
            f1, f2 = f2, f1 + f2
            stsirs += 1

        return f2

