class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #by default its a mean heap
        max_heap = []
        dic = {}

        # get frequency of characters
        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        # add the (freq, value) to the maxheap
        for key, val in dic.items():
            heapq.heappush(max_heap, (-val, key))
        
        return [ heapq.heappop(max_heap)[1] for _ in range(k)]
