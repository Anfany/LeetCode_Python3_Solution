# -*- coding：utf-8 -*-
# &Author  AnFany

# 771_Jewels_and_Stones  宝石与石头



class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # 需要遍历石头的字符串，并且判断字符是否在宝石中，因此为了查询的效率，宝石字符串要变为字典

        jewels_dict = {j: 0 for j in J}

        # 石头字符串为空集
        if not S:
            return 0

        jewels_count = 0

        for s in S:
            if s in jewels_dict:  # 判断是否是宝石
                jewels_count += 1
        return jewels_count







