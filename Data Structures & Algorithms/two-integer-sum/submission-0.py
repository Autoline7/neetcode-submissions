class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key = Index value, value = position
        dic = {}
        l = 0
        r = 0

        for i in range(len(nums)):
            curr = nums[i]
            complement = target - nums[i]
            if complement in dic:
                return [dic[complement], i]
            dic[curr] = i
        return []
        