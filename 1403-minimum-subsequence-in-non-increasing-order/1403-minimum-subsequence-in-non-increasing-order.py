class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        answer = nums
        if len(nums) == 1:
            return answer
        nums.sort(reverse=True)
        for i in range(1, len(nums)):
            if sum(nums[:i]) > sum(nums[i:]):
                answer = nums[:i]
                break
        return answer
