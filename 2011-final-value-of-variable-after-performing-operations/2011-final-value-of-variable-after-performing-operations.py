class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for elem in operations:
            if elem in ["--X", "X--"]:
                res -= 1 
            elif elem in ["X++","++X"]:
                res += 1
        return res