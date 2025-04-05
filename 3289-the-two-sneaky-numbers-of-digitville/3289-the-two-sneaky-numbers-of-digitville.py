class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        known_nums = []
        res = []
        for el in nums:
            if el in known_nums:
                res.append(el)
            else:
                known_nums.append(el)
        return res

        