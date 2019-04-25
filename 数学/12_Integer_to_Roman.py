# -*- coding：utf-8 -*-
# &Author  AnFany

# 12_Integer_to_Roman  整数转罗马数字



class Solution:
    def __init__(self):
        self.roman_integer_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    def intToRoman(self, num: int) -> str:
        # 挨个数字进行判断
        # 首先将数字变为字符串
        str_num = str(num)

        # 然后将数字中的每个字符变为字典中存在的数字
        number_list = []
        len_num = len(str_num)
        for n in range(len_num):
            int_num = int(str_num[n])
            # 和5进行比较
            l = int_num // 5
            c = int_num % 5
            # 位数，个、十、百………
            carry = len_num - n - 1

            if l:  # 大于等于5

                if c == 4:  # 说明此数为9
                    number_list.append([10 ** carry, 1])
                    number_list.append([10 ** (carry + 1), 1])
                else:
                    if c:
                        number_list.append([5 * 10 ** carry, 1])
                        number_list.append([10 ** carry, c])
                    else:  # 此数为5
                        number_list.append([5 * 10 ** carry, 1])
            else:  # 小于5
                if c == 4:  # 此数为4
                    number_list.append([10 ** carry, 1])
                    number_list.append([5 * 10 ** carry, 1])
                else:
                    number_list.append([10 ** carry, c])

        # 新的字符串
        roman_str = ''

        for i in number_list:
            roman_str += self.roman_integer_dict[i[0]] * i[1]

        return roman_str




