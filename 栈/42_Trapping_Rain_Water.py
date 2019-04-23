# -*- coding：utf-8 -*-
# &Author  AnFany

# 42_Trapping_Rain_Water 接雨水


class Solution:
    # 计算左峰高度低于等于右峰高度组成的低洼区域，获取低洼区域后，再计算可以接雨水的多少
    def get_water(self, height, equal=True):
        start_height = height[0]  # 开始的高度

        water = 0  # 可以接水的多少

        left_sign = 0  # 判断左峰是否存在的标识

        each_water = 0  # 每一块低洼区域可以接的雨水

        for h in height[1:]:
            if h < start_height:  # 开始出现低洼
                each_water += start_height - h  # 这一块可以接的雨水
                left_sign = 1  # 左峰存在
            elif h > start_height or (h == start_height and equal):   # 防止重复计算
                if left_sign:  # 如果左峰存在，此时又出现了右峰，说明低洼区域已经形成
                    water += each_water  # 添加这块低洼区域可以接的雨水
                    # 在进行下一个的低洼区域的判断
                    left_sign = 0
                    each_water = 0  # 每一块低洼区域可以接的雨水
                start_height = h  # 新的开始的高度
        return water

    def trap(self, height: List[int]) -> int:
        # 需要计算左峰高度低于等于右峰高度组成的低洼区域
        # 以及右峰高度低于左峰高度组成的低洼区域
        # 因此需要将数组反转，计算两者之和，注意反转序列不用计算左右峰高度相等的情况，会计算重复
        if len(height) <= 2:
            return 0
        return self.get_water(height) + self.get_water(height[::-1], False)


