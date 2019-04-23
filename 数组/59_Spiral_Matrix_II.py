# -*- coding：utf-8 -*-
# &Author  AnFany

# 59_Spiral_Matrix_II 螺旋矩阵II


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 也就是按照右、下、左、上的方向循环放置数字
        # 首先新建二维列表，如下形式建立，不可以用[list(range(n)]*n的形式，是为了防止赋值出现错误
        spiral_matrix = [[0 for i in range(n)] for i in range(n)]
        # 继续填充的标识
        fill_sign = 1
        # 填充的第一个数
        fill_numer = 1
        # 开始填充的位置
        c, l = 0, 0
        # 已经填充的位置
        fill_dict = {}

        while fill_sign:
            fill_sign = 0
            # 首先向右填充
            while l < n and (c, l) not in fill_dict :
                spiral_matrix[c][l] = fill_numer  # 填充数
                fill_numer += 1  # 数加1
                fill_sign = 1  # 填充标识符号
                fill_dict[(c, l)] = 0
                l += 1  # 列索引加1
            if not fill_sign:  # 只要不能填充，就说明填充完毕
                break
            # 此时行要加1,列减去刚才循环中加的1
            c += 1
            l -= 1

            # 然后向下填充
            while c < n and (c, l) not in fill_dict :
                spiral_matrix[c][l] = fill_numer  # 填充数
                fill_numer += 1  # 数加1
                fill_sign = 1  # 填充标识符号
                fill_dict[(c, l)] = 0
                c += 1  # 行索引加1
            if not fill_sign:  # 只要不能填充，就说明填充完毕
                break
            # 此时列要减1，行减去刚才循环中加的1
            l -= 1
            c -= 1

            # 然后向左填充
            while l >= 0 and (c, l) not in fill_dict :
                spiral_matrix[c][l] = fill_numer  # 填充数
                fill_numer += 1  # 数加1
                fill_sign = 1  # 填充标识符号
                fill_dict[(c, l)] = 0
                l -= 1  # 列索引减1
            if not fill_sign:  # 只要不能填充，就说明填充完毕
                break
            # 此时行要减1，列加上刚才循环中减的1
            c -= 1
            l += 1

            # 然后向上填充
            while c >= 0 and (c, l) not in fill_dict:
                spiral_matrix[c][l] = fill_numer  # 填充数
                fill_numer += 1  # 数加1
                fill_sign = 1  # 填充标识符号
                fill_dict[(c, l)] = 0
                c -= 1  # 行索引减1
            if not fill_sign:  # 只要不能填充，就说明填充完毕
                break
            # 此时列要加1，行加上刚才循环中减的1
            l += 1
            c += 1

        return spiral_matrix
