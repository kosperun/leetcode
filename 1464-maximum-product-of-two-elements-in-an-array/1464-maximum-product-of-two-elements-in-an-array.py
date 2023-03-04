class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ = 0
        for i, el in enumerate(nums):
            for j, item in enumerate(nums):
                if i != j and (nums[i]-1)*(nums[j]-1) > max_:
                    max_ = (nums[i]-1)*(nums[j]-1)
        return max_