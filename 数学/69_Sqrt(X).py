# -*- coding：utf-8 -*-
# &Author  AnFany

# 69_Sqrt(X) X的平方根


class Solution:
    def mySqrt(self, x: int) -> int:
        min_num = 0  # 查找的最小值
        max_num = x  # 查找的最大值

        while min_num < max_num:
            middle = (min_num + max_num) / 2
            # 开始进行二分查找

            if middle ** 2 < x:
                min_num = middle

            elif middle ** 2 > x:
                max_num = middle

            else:
                return int(middle)

            if int(max_num) == int(min_num):  # 最大值，最小值整数部分相同，就返回结果
                return int(min_num)

        return int(min_num)



