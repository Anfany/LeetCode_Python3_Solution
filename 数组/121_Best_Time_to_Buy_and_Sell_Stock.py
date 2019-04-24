# -*- coding：utf-8 -*-
# &Author  AnFany

# 121_Best_Time_to_Buy_and_Sell_Stock 买卖股票的最佳时机

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 利用动态规划的方法，
        # 价格序列是空集
        if not prices:
            return 0
        profit = 0  # 存储利润

        buy_prices = max(prices) + 1  # 开始的进价

        for p in prices:
            if p < buy_prices:  # 只要低于进价，就更新进价
                buy_prices = p
            elif p > buy_prices:  # 只要大于进价，就计算利润
                profit = max(profit, p - buy_prices)

        return profit





