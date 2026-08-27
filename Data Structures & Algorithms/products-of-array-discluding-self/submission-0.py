class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        
        postfix = [0] * n
        
        postfix[n-1] = nums[n-1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]

        # build final answer

        # [1, 2, 8, 48]
        # [48, 48, 24, 6]

        #prefix -> mult left to right
        #postfix -> mult right to left
        # ans -> one pointer left (from prefix) * one pointer right (from postfix)
        # ans at beg and end only use 1 pointer

        ans = [0] * n
        # mult from right
        ans[0] = postfix[1]
        #mult from left
        ans[n-1] = prefix[n-2]
        for i in range(1, n-1):
            ans[i] = prefix[i-1] * postfix[i+1]

        return ans

