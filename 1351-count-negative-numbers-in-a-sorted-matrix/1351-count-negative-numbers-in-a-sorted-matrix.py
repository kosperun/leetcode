class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for el in grid:
            for num in el:
                if num < 0:
                    cnt += 1
        return cnt