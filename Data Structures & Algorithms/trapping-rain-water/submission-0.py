class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        left_max = 0
        r = len(height)-1
        right_max = 0

        total = 0

        while l < r:

            if height[l] < height[r]:
            #work on left side
                left_area = max(0, left_max - height[l])
                total += left_area
                left_max = max(left_max, height[l])
                l += 1
            else:
            # work on right side
                right_area = max(0, right_max - height[r])
                total += right_area
                right_max = max(right_max, height[r])
                r -= 1
        
        return total