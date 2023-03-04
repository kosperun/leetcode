class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = {}
        for el in nums:
            if el in res:
                res[el] += 1
            else:
                res[el] = 1
        fin = []
        for k, v in res.items():
            if v == 1:
                fin.append(k)
        return sum(fin)

 
