"""
時間計算量 : O(n), 86.94%
空間計算量 : O(1), 64.49%
"""

from typing import List

class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell

        return profit