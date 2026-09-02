class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # sliding window

        l = 0
        curr_min = prices[0]
        ans = 0
        r = 0
        
        while r < len(prices):
            price = prices[r]

            # new min so we update curr min
            if curr_min > price:
                curr_min = price
                l = r
            
            ans = max(ans, price-prices[l])
            r += 1

        return ans

        