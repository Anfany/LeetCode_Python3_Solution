# -*- coding：utf-8 -*-
# &Author  AnFany

# 119_Pascal's_Triangle_II 杨辉三角II


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        # 开始的行数
        start_num = 0

        result = [1]  # 等于0时的结果

        while start_num < rowIndex:

            # 前面加0元素构成的列表
            forward_list = [0] + result

            # 后面加0元素构成的列表
            back_list = result + [0]

            # 两个列表对元素求和即可得到新的行
            result = [i + j for i, j in zip(forward_list, back_list)]

            # 行数加1
            start_num += 1

        return result


