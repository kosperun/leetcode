class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for op in operations:
            if op == '+':
                new = res[-1] + res[-2]
                res.append(new)
            elif op == 'D':
                res.append(res[-1]*2)
            elif op == 'C':
                res.pop()
            try:
                res.append(int(op))
            except ValueError:
                continue
        return sum(res)

