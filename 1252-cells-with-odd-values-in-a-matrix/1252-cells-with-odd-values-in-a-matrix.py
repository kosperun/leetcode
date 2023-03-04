class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for i in range(n)] for j in range(m)]
        for el in indices:
            # Increment rows:
            for i in range(n):
                # for elem in i:
                matrix[el[0]][i] += 1
            # Increment columns
            for i in range(m):
                # for elem in i:
                matrix[i][el[1]] += 1
        cnt = 0
        for row in matrix:
            for num in row:
                if num % 2 != 0:
                    cnt += 1
        return cnt
