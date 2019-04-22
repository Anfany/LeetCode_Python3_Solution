# -*- coding：utf-8 -*-
# &Author  AnFany
# 319_Bulb_Switcher 灯泡开关

"""
class Solution:
    def bulbSwitch(self, n: int) -> int:
        bulb_list = [1] * n  # 第一轮，所有的灯都是开启状态
        # 开始模拟切换开关的状态
        for i in range(2, n + 1):
            for index in range(i, n + 1):
                if index % i == 0:
                    bulb_list[index - 1] = -bulb_list[index - 1]
        #  返回数组中元素为1的个数
        return int((n + sum(bulb_list)) / 2)
"""


class Solution:
    def bulbSwitch(self, n: int) -> int:
        # 从第一轮的状态开始，对第i个灯泡的切换开关次数进行统计，只要它再经历偶数次开关，最后就是亮着的。
        # 也就是说对于i而言，只要其不为1的因子有偶数个，其最后就是亮着的。
        # 也就是说对于i而言，只要其因子有奇数个，其最后就是亮着的。
        # 对于数i而言，只要它是平方数，他的因子数肯定为奇数个
        # 因此只要计算从1到n，是平方数的个数有多少即可
        # 从1到n的平方数的个数就为n的平方根的整数部分个
        return int(n ** 0.5)





