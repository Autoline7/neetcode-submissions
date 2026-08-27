class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter to get frequency O(n)
        count = Counter(nums)

        # by default its a min heap
        # use heapify to add to min heap O(m), where m is unique numbers
        max_heap = [(-freq, val) for val, freq in count.items()]
        heapq.heapify(max_heap)

        # return the top k in the max heap O(k * log(m))
        return [heapq.heappop(max_heap)[1] for _ in range(k)]
