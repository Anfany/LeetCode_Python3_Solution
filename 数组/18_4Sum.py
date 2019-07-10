# -*- coding：utf-8 -*-
# &Author  AnFany

# 18_4sum 四数之和

# 思路类似于15三数之和


class Solution:
    def fourSum(self, nums, target):
        # 如果nums为空
        if not nums:
            return []
        # 将数据序列排序
        nums.sort()
        length = len(nums)
        result = []  # 最终的结果
        # 先选中一个one
        for one in range(length - 3):
            # 在选中第二个two
            for two in range(length - 1, 2 + one, -1):
                # 固定2个，寻找第三个和第四个
                three = one + 1
                four = two - 1
                while three < four:
                    # 计算四者的和
                    number_sum = nums[one] + nums[two] + nums[three] + nums[four]
                    # 如果为0
                    if number_sum == target:
                        # 添加到结果中
                        result.append([nums[one], nums[two], nums[three], nums[four]])
                        three += 1
                        four -= 1
                    # 如果大于0，four对应的变小
                    elif number_sum > target:
                        four -= 1
                    # 如果小于0，three对应的变大
                    else:
                        three += 1
        # 删除掉重复的
        last_result = []
        for h in result:
            if h not in last_result:
                last_result.append(h)
        return last_result


