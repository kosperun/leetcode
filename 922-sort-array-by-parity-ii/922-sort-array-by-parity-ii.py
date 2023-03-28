class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evens = [el for el in nums if el % 2 == 0]
        odds = [el for el in nums if el % 2 != 0]
        result = [item for pair in zip(evens, odds) for item in pair]
        return result