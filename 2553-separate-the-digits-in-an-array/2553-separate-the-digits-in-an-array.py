class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        temp = "".join([str(i) for i in nums])
        return [int(i) for i in temp]