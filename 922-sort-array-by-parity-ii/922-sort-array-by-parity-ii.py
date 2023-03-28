class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        return [item for pair in zip([el for el in nums if el % 2 == 0], [el for el in nums if el % 2 != 0]) for item in pair]
        