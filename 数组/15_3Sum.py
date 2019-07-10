# -*- coding：utf-8 -*-
# &Author  AnFany

# 15_3sum 三数之和


class Solution:
    def threeSum(self, nums):
        # 如果nums为空
        if not nums:
            return []
        # 将数据序列排序
        nums.sort()
        length = len(nums)
        result = [] # 最终的结果
        # 先选中一个one
        for one in range(length):
            if one > 0 and nums[one] == nums[one-1]:  # 防止出现重复序列
                continue
            two = one + 1
            three = length - 1
            # 固定one，寻找第二个和第三个
            while two < three:
                # 计算三者的和
                cur_sum = nums[one] + nums[two] + nums[three]
                # 如果为0
                if cur_sum == 0:
                    # 添加到结果中
                    result.append([nums[one], nums[two], nums[three]])
                    # 防止出现重复的序列
                    while two < three and nums[two] == nums[two+1]:
                        two += 1
                    while two < three and nums[three] == nums[three-1]:
                        three -= 1
                    # two对应的需要变大，three对应的需要变小。
                    two += 1
                    three -= 1
                # 如果大于0，three对应的变小
                elif cur_sum > 0:
                    three -= 1
                # 如果小于0，two对应的变大
                else:
                    two += 1
        return result