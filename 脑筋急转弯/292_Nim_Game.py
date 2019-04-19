# -*- coding：utf-8 -*-
# &Author  AnFany
# 292_Nim_Game Nim游戏


class Solution:
    def canWinNim(self, n: int) -> bool:
        # 最后剩下4块石头时，谁先拿谁输，因此：
        # 只要我第一次拿完后，剩下的石头的块数可以被4整除，我就可以赢
        # 因为以后的每一次我都可以拿去(4-对方刚才拿的块数)块石头

        if n % 4 == 0:
            return False
        else:
            return True