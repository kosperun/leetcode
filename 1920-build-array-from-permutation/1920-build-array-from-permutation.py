class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0 for elem in nums]
        for i, elem in enumerate(nums):
            ans[i] = nums[elem]
        return ans