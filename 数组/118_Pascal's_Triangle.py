# -*- coding：utf-8 -*-
# &Author  AnFany

# 118_Pascal's_Triangle 杨辉三角


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # 当行数为0时
        if not numRows:
            return []
        
        # 开始的行数
        start_num = 1

        # 存储最终的结果
        result = [[1]]  # 等于1时的结果

        while start_num < numRows:
            last_row = result[-1]

            # 前面加0元素构成的列表
            forward_list = [0] + last_row

            # 后面加0元素构成的列表
            back_list = last_row + [0]

            # 两个列表对元素求和即可得到新的行
            new_row = [i + j for i, j in zip(forward_list, back_list)]

            # 添加到结果中
            result.append(new_row)

            # 行数加1
            start_num += 1

        return result

