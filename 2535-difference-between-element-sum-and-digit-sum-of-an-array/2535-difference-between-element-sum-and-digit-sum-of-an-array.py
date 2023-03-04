class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem_sum = sum(nums)
        nums_str = ''.join([str(elem) for elem in nums])
        dig_sum = 0
        for elem in nums_str:
            dig_sum += int(elem)
        return abs(elem_sum - dig_sum)