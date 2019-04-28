# -*- coding：utf-8 -*-
# &Author  AnFany

# 9_Palindrome_Number 回文数


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数肯定不是回文数
        if x < 0:
            return False
        elif x == 0:  # 0 肯定是回文数
            return True
        else:
            if x % 10 == 0:   # 结尾是0,并且大于0的数肯定不是回文数
                return False
            else:
                # 获取这个数的反转。不用全部反转，
                # x的长度为偶数的反转一半即可，为奇数的反转一半减1即可
                # 首先获取数的长度
                length = 0
                while 10 ** length < x:
                    length += 1

                #  一位的肯定是回文数
                if length == 1:
                    return True

                # 开始判断
                start_carry = 1

                # 计算前面的数字和计算后面数字要用到的x
                f_x, b_x = x, x
                while start_carry <= length // 2:
                    # 后面的数字
                    back_number = b_x % 10
                    b_x = b_x // 10

                    # 前面的数字
                    forward_number = f_x // (10 ** (length - start_carry))
                    f_x = f_x % (10 ** (length - start_carry))

                    start_carry += 1

                    if back_number != forward_number:
                        return False

                return True


