class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        if target not in nums:
            return res
        first = nums.index(target)
        while first < len(nums) and nums[first] == target:
            res.append(first)
            first += 1
        return res