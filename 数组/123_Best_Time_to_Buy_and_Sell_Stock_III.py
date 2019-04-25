# -*- coding：utf-8 -*-
# &Author  AnFany

# 123_Best_Time_to_Buy_and_Sell_Stock_III 买卖股票的最佳时机III


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        length_prices = len(prices)
        # 为空集时
        if not length_prices:
            return 0

        # 也就是寻找一天T，使得第1天到第T天可以达到的最大利润值
        # 与第T天到最后1天可以达到的最大利润值
        # 的和最大

        # 获得第1天到第T天的可以达到的最大利润值
        # 也就是在正向的价格列表中获得最大利润序列max_profit
        buy_price = prices[0]
        max_profit = [0]
        for p in prices[1:]:
            if p > buy_price:
                max_profit.append(max(max_profit[-1], p - buy_price))
            else:
                buy_price = p
                max_profit.append(max_profit[-1])  # 之前出现的最大的利润值

        # 获得第T天到最后1天的可以达到的最大利润值
        # 也就是在反转的价格列表中获得最小的利润序列min_profit
        prices = prices[::-1]  # 反转
        buy_price = prices[0]
        min_profit = [0]
        for p in prices[1:]:
            if p < buy_price:
                min_profit.append(min(min_profit[-1], p - buy_price))
            else:
                buy_price = p
                min_profit.append(min_profit[-1])

        # 注意最小的利润序列需要反转过来
        return max([max_p - min_p for max_p, min_p in zip(max_profit, min_profit[::-1])])

