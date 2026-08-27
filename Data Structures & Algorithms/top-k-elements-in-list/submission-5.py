class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        min_heap = []

        # O(n)
        count = Counter(nums)

        # O(m), where m is the number of unique numbers
        for num, freq in count.items():
            # O(log(k))
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                # O(log(k))
                heapq.heappop(min_heap)
        
        # O(k)
        return [num[1] for num in min_heap]

        # Total Time: O(m * log(k))