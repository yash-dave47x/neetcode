class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        prev_price=prices[0]
        for price in prices:
            if prev_price>= price:
                prev_price= price
                continue
            temp = price-prev_price
            if temp> max_profit:
                max_profit= temp
        return max_profit