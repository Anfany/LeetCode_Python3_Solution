# -*- coding：utf-8 -*-
# &Author  AnFany

# 121_Best_Time_to_Buy_and_Sell_Stock 买卖股票的最佳时机

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 价格序列是空集
        if not prices:
            return 0
        better_price = [0]  # 存储比较好的价格
        low_price, up_price = prices[0], prices[0]  # 可看作初始的进价、卖价
        buy_sign = 0  # 买进的标识
        for p in prices[1:]:
            if not buy_sign:
                if p > low_price:  # 只有小值后面出现了大值，才能买进，也就是买进标识才为1
                    up_price = p
                    buy_sign = 1
                else:  # 否则的话，只能继续寻找
                    low_price = p
                    up_price = p
            else:
                if p > up_price:  # 当买进标识为1时，只要遇见比最大值大的，就更新最大值
                    up_price = p
                elif p < low_price:  # 只要遇见比最小值小的，就存储截止到目前的利润
                    better_price.append(up_price - low_price)
                    low_price = p   # 再次更新最大值，最小值，
                    up_price = p
                    buy_sign = 0  # 同时买进标识设置为0
        if buy_sign:  # 最后，只要买进标识为1，就存储利润
            better_price.append(up_price - low_price)
        return max(better_price)




