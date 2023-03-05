class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # arr_d = {}
        # for el in arr:
        #     if el in arr_d:
        #         arr_d[el] += 1
        #     else:
        #         arr_d[el] == 1
        return sorted(arr) == sorted(target)
        