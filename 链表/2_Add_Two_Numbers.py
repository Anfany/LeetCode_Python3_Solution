# -*- coding：utf-8 -*-
# &Author  AnFany
# 2_Add_Two_Numbers 两数相加


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode(0)  # 定义一个首节点为0的链表
        carry = 0  # 表示进位
        sum_listnode = head  # 最终结果的链表

        while carry or l1 or l2:  # 只要有一个非空就循环
            node = ListNode(carry)  # 前一个进位的数字的链表

            if l1:
                node.val += l1.val  # 加上l1的数字
                l1 = l1.next  # 更新l1
            if l2:
                node.val += l2.val  # 加上l2的数字
                l2 = l2.next  # 更新l2

            carry = node.val // 10  # 进位
            node.val %= 10  # 进位后余下的数

            head.next, head = node, node

        return sum_listnode.next  # 除去首节点的链表

