class Solution:
    def judgeCircle(self, moves: str) -> bool:
        res = [0, 0]
        for el in moves:
            if el == "U":
                res[0] += 1
            elif el == "D":
                res[0] -= 1
            elif el == "R":
                res[1] += 1
            elif el == "L":
                res[1] -= 1
        return res == [0, 0]