class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        l = 0
        r = len(nums)-1
        ans = [-1,-1]
        while l <= r:
            mid = l + (r-l) // 2

            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            
            if nums[mid] == target:
                first = mid
                
                while first > 0 and nums[first-1] == target:
                    first -= 1
                
                last = mid
                while last < len(nums)-1 and nums[last+1] == target:
                    last += 1
                
                ans = [first, last]
                return ans
        
        return ans