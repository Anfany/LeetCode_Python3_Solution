# -*- coding：utf-8 -*-
# &Author  AnFany

# 41_First_Missing_Positive 缺失的第一个正数


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 数组的长度
        length = len(nums)
        # 首先创建一个和数组nums一样长的数组
        new_nums = [0] * length

        # 将数组nums中，满足要求的数值，按序存储到新的数组中
        for i in nums:
            if 0 < i <= length:  # 小于等于0的不用存储，某个数值大于数组长度，也不需要存储，因为缺失的正数肯定小于该值
                new_nums[i - 1] = i

        #  再次遍历数组，只要索引加1与值不符合，则说明是缺失的
        for index, value in enumerate(new_nums):
            if index + 1 != value:
                return index + 1
        # 说明缺失的是最后一个值
        return length + 1