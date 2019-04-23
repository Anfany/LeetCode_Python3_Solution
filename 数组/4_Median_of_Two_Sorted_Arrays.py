# -*- coding：utf-8 -*-
# &Author  AnFany

# 4_Median_of_Two_Sorted_Arrays 寻找两个有序数组的中位数


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 将数组nums1,nums2分别拆分为2左右2部分，分别记为L1,R1,L2,R2
        # 只要满足以下的条件，就可以得到中位数
        # (1)：L1和L2的长度和 与 R1和R2的长度和 的差 为0或者-1
        # (2)：L1和L2的最大值要小于等于 R1和R2的最小值, 因为数组都是有序的
        # 也就是L1的最后的值不大于R2的第一个值，L2的最后的值不大于R1的第一个值
        # 现在的重点就在于如何将数组各自分割为2部分，
        # 因为要保证分割后的2部分的长度是一样的，因此决定了一个数组的分割点，另一个也就自然决定了
        # 为了效率，我们先确定数组长度较短的分割点

        len_nums1, len_nums2 = len(nums1), len(nums2)

        # 首先判断存在空数组的情况
        if not len_nums1:
            middle = len_nums2 // 2
            if len_nums2 % 2 == 0:
                return (nums2[middle] + nums2[middle - 1]) / 2
            else:
                return nums2[middle]

        if not len_nums2:
            middle = len_nums1 // 2
            if len_nums1 % 2 == 0:
                return (nums1[middle] + nums1[middle - 1]) / 2
            else:
                return nums1[middle]

        # 对于均不为空的情况，
        if len_nums1 > len_nums2:
            min_len, max_len, short_list, long_list = len_nums2, len_nums1, nums2, nums1
        else:
            min_len, max_len, short_list, long_list = len_nums1, len_nums2, nums1, nums2

        # 编程便利性，为了避免L1，L2 R1 R2出现空集的情况
        max_number = max(short_list[-1], long_list[-1])
        min_number = min(short_list[0], long_list[0])
        short_list.insert(0, min_number - 1)
        short_list.append(max_number + 1)
        long_list.insert(0, min_number - 1)
        long_list.append(max_number + 1)

        min_split = 0  # 最小的分割点
        max_split = min_len
        all_length = min_len + max_len

        while min_split <= max_split:
            # 较短的数组的分割点
            middle_split = (min_split + max_split) // 2

            # 较长数组的分割点为
            long_split = (len_nums1 + len_nums2 + 4) // 2 - middle_split - 2

            # 较短数组分割点2边的值
            s_l, s_r = short_list[middle_split], short_list[middle_split + 1]

            # 较长数组分割点2边的值
            l_l, l_r = long_list[long_split], long_list[long_split + 1]

            # 开始判断
            if s_l <= l_r and l_l <= s_r:
                # 说明找到了
                if all_length % 2 == 0:
                    left_number = max(s_l, l_l)
                    right_number = min(s_r, l_r)
                    return (left_number + right_number) / 2
                else:
                    return min(l_r, s_r)

            elif s_l > l_r and l_l <= s_r:
                # 说明较短的数组的分割点需要变小
                max_split -= 1
            elif s_l <= l_r and l_l > s_r:
                # 说明较长的数组的分割点需要变小，也就是较短的分割点需要变大
                min_split += 1









