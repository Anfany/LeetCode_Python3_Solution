# -*- coding：utf-8 -*-
# &Author  AnFany

# 54 Spiral_Matrix 螺旋矩阵


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # matrix为空集
        if not matrix:
            return matrix
        # 获得m，n
        m, n = len(matrix), len(matrix[0])

        # 走过的位置用字典存储
        poss_dict = {}

        # 最终返回的列表
        poss_list = []

        # 从(0,0)开始出发，然后依次按照右、下、左、上的方向循环，
        # 当到达边界或者要去的位置已经走过时，则改变方向
        # 当要去的方向的位置已经走过时，就停止

        start_m, start_n = 0, -1  # 对于只有一列的矩阵，设置为-1，保证开始是向右走的

        stop_sign = 1  # 判断是否停止的标识

        while stop_sign:
            stop_sign = 0
            # 向右走
            while start_n < n - 1 and (start_m, start_n + 1) not in poss_dict:
                start_n += 1
                poss_dict[(start_m, start_n)] = 0
                poss_list.append(matrix[start_m][start_n])
                stop_sign = 1
            
            if not stop_sign:
                break

            # 向下走
            while start_m < m - 1 and (start_m + 1, start_n) not in poss_dict:
                start_m += 1
                poss_dict[(start_m, start_n)] = 0
                poss_list.append(matrix[start_m][start_n])
                stop_sign = 1
                
            if not stop_sign:
                break
    
                

            # 向左走
            while start_n > 0 and (start_m, start_n - 1) not in poss_dict:
                start_n -= 1
                poss_dict[(start_m, start_n)] = 0
                poss_list.append(matrix[start_m][start_n])
                stop_sign = 1
            
            if not stop_sign:
                break


            # 向上走
            while start_m > 0 and (start_m - 1, start_n) not in poss_dict:
                start_m -= 1
                poss_dict[(start_m, start_n)] = 0
                poss_list.append(matrix[start_m][start_n])
                stop_sign = 1
                
            if not stop_sign:
                break

        return poss_list


