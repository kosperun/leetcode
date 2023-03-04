class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        while any(nums):
            nums.sort()
            smallest = next(filter(lambda x: x > 0, nums))
            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] -= smallest
            cnt += 1
        return cnt