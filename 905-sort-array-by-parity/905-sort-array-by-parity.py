class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for el in nums:
            if el % 2 == 0:
                even.append(el)
            else:
                odd.append(el)
        even.extend(odd)
        return even