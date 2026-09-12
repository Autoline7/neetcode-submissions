class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 1 or k == 1:
            return nums
        
        if len(nums) == 2:
            return [max(nums[0], nums[1])]

        # use heap to keep track of max

        # when popping non-max -> dont pop
        # when max needs to get popped -> keep popping until the index is within bounds

        heap = []
        ans = [0] * len(nums)

        for r in range(k):
            heapq.heappush(heap, (-nums[r], r))
        
        
        a = 0
        ans[a] = -heap[0][0]

        # loop
        for r in range(k, len(nums)):

            # push to max-heap (value, index)
            heapq.heappush(heap, (-nums[r], r))

            # keep popping until 
            l = r - k + 1
            while l > heap[0][1]:
                heapq.heappop(heap)
            
            a += 1
            ans[a] = -heap[0][0]
            

        return ans[:a+1]






