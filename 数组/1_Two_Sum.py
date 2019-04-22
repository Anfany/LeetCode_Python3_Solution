# -*- coding：utf-8 -*-
# &Author  AnFany
# 1_Two_Sum 两数之和


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建nums中的值与索引的字典
        nums_dict = {}
        for i in range(len(nums)):
            number = nums[i]
            if target - number in nums_dict:
                return [nums_dict[target - number], i]
            else:
                nums_dict[number] = i

