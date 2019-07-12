# -*- coding：utf-8 -*-
# &Author  AnFany

# 19_Remove Nth Node From End of List 删除链表的倒数第N个节点


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# # 定义四个节点
# a = ListNode(86)
# b = ListNode(19)
# c = ListNode(4)
# d = ListNode(12)
# # 最简单的方法将四个节点连接
# a.next = b
# b.next = c
# c.next = d
# head = a
# while head is not None:
#     print(head.val)
#     print(head.next)
#     head = head.next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #  采用双指针，第一个指针和第二个指针之间要正好差n+1个，这样第二个指针到最后的时候，第一个指针的.next恰好在需要删除的节点的前面
        front_node = head

        back_node = head

        # 间隔n个
        for h in range(n):
            front_node = front_node.next

        # 如果front_node到了最后，说明需要删除的是头节点
        if not front_node:
            return head.next
        else:
            # 此时间隔n+1个
            front_node = front_node.next

        # 开始移动2个指针，当前面的指针到达最后，也就是值为None时
        while front_node:
            front_node = front_node.next
            back_node = back_node.next
        # 删除需要去掉的节点
        back_node.next = back_node.next.next
        # 返回此时的链表
        return head






















































































