# -*- coding：utf-8 -*-
# &Author  AnFany

# 885_Spiral_Matrix_II 螺旋矩阵III


class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        #  所有网格的总数
        cells = R * C
        if not cells:
            return []

        # 对于索引为(r,l)的网格，计算从初始网格到这个网格的步数，然后将网格按照步数从小到大排序
        # 假设初始点为0,0
        # 如果r+l=0，并r>l，则到达该网格的步数为(r-l)^2，偶数的平方
        # 如果r+l=1，并r<l，则到达该网格的步数为(r-l)^2，奇数的平方
        # 到达其他任意的网格的步数，都可以据此得出
        # 如图所示，红色的利用偶数的平方推导步数，蓝色的利用奇数的平方推导步数

        cell_step_dict = {}

        for a in range(R):
            for b in range(C):
                r, l = a - r0, b - c0
                # 判断，利用偶数还是奇数
                if r >= l:  # 利用偶数平方
                    max_num = max(abs(r), abs(l))
                    # 偶数平方
                    squre = (2 * max_num) ** 2
                    step = squre - (r + l)
                else:  # 利用奇数平方
                    if abs(r) >= abs(l):
                        max_num = 2 * abs(r) + 1
                    else:
                        max_num = 2 * abs(l) - 1
                    # 奇数平方
                    squre = max_num ** 2
                    step = squre + (r + l - 1)
                cell_step_dict[step] = [a, b]
        # 按照步数从小到大排序
        result = [c[1] for c in sorted(cell_step_dict.items(), key=lambda x: x[0])]

        return result

