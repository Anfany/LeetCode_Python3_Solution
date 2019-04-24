# -*- coding：utf-8 -*-
# &Author  AnFany

# 122_Best_Time_to_Buy_and_Sell_Stock_II 买卖股票的最佳时机II


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 初始买进标识为0，当后面出现的值大于前面的值时，买进标识变为1，
        # 之前的小值记录为进价，之后的大值记录为出价。
        # 只要后面出现的值小于出价，就计算利润。然后开始新的买进标识判断
        # 如果大于出价，则跟更新出价

        if not prices:
            return 0  # 价格序列为空

        buy_sign = 0  # 买进标识

        buy_price, sell_price = prices[0], prices[0]  # 初始的进价、出价

        profit = 0  # 总共的利润

        for p in prices[1:]:
            if not buy_sign:  # 买进标识为0
                if p > buy_price:  # 只要大于进价
                    sell_price = p  # 将此价定义为出价
                    buy_sign = 1   # 买进标识为1
                else:
                    buy_price, sell_price = p, p
            else:
                if p < sell_price:
                    profit += sell_price - buy_price
                    buy_price, sell_price = p, p
                    buy_sign = 0
                else:
                    sell_price = p

        if buy_sign:
            profit += sell_price - buy_price

        return profit


