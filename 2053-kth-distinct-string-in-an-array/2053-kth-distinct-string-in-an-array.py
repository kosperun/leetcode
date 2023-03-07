class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dist = {}
        for el in arr:
            if arr.count(el) in dist:
                dist[arr.count(el)].append(el)
            else:
                dist[arr.count(el)] = [el]
        if 1 not in dist or len(dist[1]) < k:
            return ""
        return dist[1][k-1]
            
            
            
            
            
            
        