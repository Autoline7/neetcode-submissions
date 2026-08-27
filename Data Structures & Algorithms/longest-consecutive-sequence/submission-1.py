class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)

        ans = 0

        for num in seen:
            
            if num-1 not in seen:
                # could be a left start point and we can iterate to find all cn
                found = num
                
                while found in seen:
                    found += 1
                 
                ans = max(ans,found-num)
        
        return ans
                