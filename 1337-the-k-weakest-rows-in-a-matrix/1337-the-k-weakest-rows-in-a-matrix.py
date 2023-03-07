class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = {i:sum(row) for i, row in enumerate(mat)}
        return sorted(res, key=lambda x: (res[x]))[:k]
            
            
        