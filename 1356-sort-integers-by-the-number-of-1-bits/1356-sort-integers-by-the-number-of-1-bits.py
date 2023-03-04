class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        nums_of_1s_map = {}
        for num in arr:
            num_of_1s = bin(num)[2:].count("1")
            if num_of_1s in nums_of_1s_map:
                nums_of_1s_map[num_of_1s].append(num)
            else:
                nums_of_1s_map[num_of_1s] = [num]
        res = []
        for _, v in sorted(nums_of_1s_map.items()):
            res.extend(sorted(v))
        return res