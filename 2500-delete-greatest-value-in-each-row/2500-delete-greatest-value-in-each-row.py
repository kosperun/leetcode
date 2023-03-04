class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0
        while all(grid):
            max_list = []
            for elem in grid:
                max_ = max(elem)
                del elem[elem.index(max_)]
                max_list.append(max_)
            res += max(max_list)
        return res