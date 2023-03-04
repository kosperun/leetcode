class Solution:
    def countPoints(self, rings: str) -> int:
        res = {}
        for i in range(0, len(rings), 2):
            if rings[i+1] in res:
                res[rings[i+1]].append(rings[i])
            else:
                res[rings[i+1]] = [rings[i]]
        cnt = 0
        for v in res.values():
            if len(set(v)) == 3:
                cnt +=1
        return cnt