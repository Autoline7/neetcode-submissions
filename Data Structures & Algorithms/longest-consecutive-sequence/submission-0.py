class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)

        ans = 0

        for num in seen:
            
            if num-1 not in seen:
                # could be a left start point and we can iterate to find all cn
                found = num
                curr_ans = 0
                while found in seen:
                    found += 1
                    curr_ans += 1
                 
                ans = max(ans,curr_ans)
        
        return ans
                