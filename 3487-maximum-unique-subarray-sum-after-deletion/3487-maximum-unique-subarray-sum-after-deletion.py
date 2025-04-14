class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if not list(filter(lambda x: x > 0, nums)):
            return sorted(nums)[-1]
        return sum(set([i for i in nums if i > 0]))
        