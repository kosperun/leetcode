class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for elem in nums:
            if elem==0:
                nums.remove(elem)
                nums.append(elem)