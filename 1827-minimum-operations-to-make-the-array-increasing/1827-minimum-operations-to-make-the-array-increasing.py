class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        prev = nums[0]
        for i in range(len(nums) - 1):
            if prev < nums[i + 1]:
                prev = nums[i + 1]
            else:
                cnt += prev + 1 - nums[i + 1]
                prev += 1
        return cnt
