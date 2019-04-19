# -*- coding：utf-8 -*-
# &Author  AnFany
# 587_Erect_The_Fence 安装栅栏


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution:
    def computer_cross_product(self, p1, p2, p3):
        """
        计算向量p1p2与p1p3的叉积
        :param p1: 点p1，转换后的坐标
        :param p2: 点p2，转换后的坐标
        :param p3: 点p3，转换后的坐标
        :return: 叉积
        """
        p1p2 = p2[0] - p1[0], p2[1] - p1[1]  # 向量p1p2
        p1p3 = p3[0] - p1[0], p3[1] - p1[1]  # 向量p1p3
        product = p1p3[0] * p1p2[1] - p1p3[1] * p1p2[0]  # 计算叉积
        return product

    def convexhull(self, point_set):
        """
        获得这些点构成的多边形的凸包，
        :param point_set: 点集，没有相同的点
        :return: 凸包上的点
        """
        # 选出所有点中纵坐标最小的点，纵坐标相同的选择横坐标最小的点
        point_set = list(point_set)
        point_set.sort(key=lambda s: [s[1], s[0]])
        min_y_point = point_set[0]  # 参考点编号为0

        # 将上面选择的点，转移到原点，计算其他所有点转移后和原点构成的向量中纵坐标除以横坐标的商
        # 根据商的不同情况，选择不用的排列策略
        # 这里将商的值分为大于等于0， 无穷，小于0三部分
        greater_equal_zero = []
        less_zero = []
        p_i = []
        for p in point_set[1:]:
            point = [p[0] - min_y_point[0], p[1] - min_y_point[1]]  # 转移后的点的坐标
            if point[0] != 0:
                tan = point[1] / point[0]
                if tan >= 0:
                    greater_equal_zero.append([tan, point[1], point, p])  # 商值，y值，转移后的值(计算凸包)，转移前的值(绘图)
                else:
                    less_zero.append([tan, point[1], point, p])  # 商值，y值，转移后的值(计算凸包)，转移前的值(绘图)
            else:
                p_i.append([0, point[1], point, p])  # 商值，y值，转移后的值(计算凸包)，转移前的值(绘图)

        # 大于等于0的首先按商升序排列，相同值但不为0的按照y的升序排列，相同值为0的按照x的升序排列(这个条件，选点的时候已经设置过，此处无需在设置)
        greater_equal_zero.sort(key=lambda m: [m[0], m[1]])
        # 小于0的首先按商升序排列，相同值的按照y的降序排列
        less_zero.sort(key=lambda m: [m[0], -m[1]])
        # 如果大于等于0的部分为空集，则按照y值的升序排列
        if not greater_equal_zero:
            p_i.sort(key=lambda m: m[1])
        else:  # 否则按照y值的降序排列
            p_i.sort(key=lambda m: -m[1])

        # 合并后，所有点是按着夹角逆时针排列的
        trans_point_angle = greater_equal_zero + p_i + less_zero  # 先是大于0，然后等于0，最后小于0，顺序不能错

        # 可知，trans_point_angle序列中的第一个点和最后一个点肯定在凸包上
        #  trans_point_angle序列开始位置添加第一个点P0
        trans_point_angle.insert(0, [0, 0, [0, 0], min_y_point])

        # trans_point_angle中的前2个点p0, p1，和最后一个点一定在凸包上
        # 把前2个点p0, p1放入栈中，把p1后面的点p2作为评判点，如果向量的叉积V_p0p2*V_p0p1<0,说明p2在p0p1的逆时针方向，是对的，如果为0，
        # 说明三点共线;如果大于0，说明p2在p0p1的顺时针方向，说明P1点是凹进去的
        # 开始挨个评判
        c = [trans_point_angle[0][2], trans_point_angle[1][2]]  # 在凸包上的点的集合
        real_c = [trans_point_angle[0][3], trans_point_angle[1][3]]  # 在凸包上的点的真正的坐标

        for index in trans_point_angle[2:]:
            c.append(index[2])
            real_c.append(index[3])

            product = self.computer_cross_product(c[-3], c[-2], c[-1])
            if product > 0:
                c.pop(-2)
                real_c.pop(-2)

                product = self.computer_cross_product(c[-3], c[-2], c[-1])

                while product > 0:
                    c.pop(-2)
                    real_c.pop(-2)
                    product = self.computer_cross_product(c[-3], c[-2], c[-1])
        return real_c

    def outerTrees(self, points: List[Point]) -> List[Point]:
        if len(points) <= 3:
            return points
        else:
            return self.convexhull(point_set=points)


















