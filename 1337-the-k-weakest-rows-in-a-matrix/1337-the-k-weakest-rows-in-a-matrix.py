class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = {}
        for i, row in enumerate(mat):
            res[i] = sum(row)
        return sorted(res, key=lambda x: (res[x]))[:k]
            
            
        