class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        firsts = {i[0] for i in paths}
        lasts = {i[1] for i in paths}
        return list(lasts.difference(firsts))[0]
                