# -*- coding：utf-8 -*-
# &Author  AnFany

# 17_Letter_Combinations_of_a_Phone_Number  电话号码的字母组合


class Solution:
    def __init__(self):
        self.digit_alpha_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits: str) -> List[str]:

        # 存储结果的列表
        combination_list = []

        # 如果digits为空
        if not digits:
            return combination_list

        # 利用回溯算法
        # 每个数字对应的状态列表，状态就是可以取的字母的索引，状态变为-1，说明已经取完
        state_list = [len(self.digit_alpha_dict[i]) - 1 for i in digits]

        inverse_str = digits[::-1]  # 电话号码的逆序字符串

        while state_list[0] != -1:  # 只要第一个不为-1，说明还有没遍历的组合

            if state_list[-1] > -1:
                #  添加组合
                new_combination = ''
                for digit, state in zip(digits, state_list):
                    new_combination += self.digit_alpha_dict[digit][state]  # 状态对应的字母
                # 将该组合添加到组合列表中
                combination_list.append(new_combination)
                # 更新状态
                state_list[-1] -= 1

            else:
                # 下面的步骤体现了回溯
                # 从最后这个位置，向前寻找状态值大于0的，这样的状态说明这个位置上的数字对应的字母没有遍历完
                inverse_list = state_list[::-1]
                # 判断是否有大于0的状态的标识
                state_sign = 0
                for s in range(len(inverse_list)):
                    if inverse_list[s] > 0:
                        inverse_list[s] -= 1
                        state_sign = 1
                        break
                    else:
                        # 这个位置之后的都要恢复到原始的状态。前面的状态改变后，后面的要恢复到初始的状态
                        inverse_list[s] = len(self.digit_alpha_dict[inverse_str[s]]) - 1

                if not state_sign:
                    break
                else:
                    state_list = inverse_list[::-1]
        return combination_list




