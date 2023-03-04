class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(grid) - 2):
            temp_res = []
            for j in range(len(grid) - 2):
                max_list = []
                for k in range(3):
                    max_list.extend(grid[i + k][j : j + 3])
                temp_res.append(max(max_list))
            res.append(temp_res)
        return res