class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == nums[j] and i < j:
                    res.append((i, j))
        return len(res)