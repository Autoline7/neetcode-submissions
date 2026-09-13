class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans = 0

        l = 0
        
        # iterate prices
        for r in range(len(prices)):

            # dec window when -> price at right is lessthan than price at left 
            # update left
            if prices[l] > prices[r]:
                l = r
            
            # inc window when -> price at right is greater or equal than price at left
            # when increasing keep track of the max profit
            ans = max(ans, prices[r]-prices[l])
        return ans
        