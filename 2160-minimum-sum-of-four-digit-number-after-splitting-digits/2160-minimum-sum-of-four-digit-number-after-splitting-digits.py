class Solution:
    def minimumSum(self, num: int) -> int:
        digits = [str(elem) for elem in str(num)]
        d = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    for m in range(len(digits)):
                        if i != j and i != k and i != m and j != k and j != m and k != m:
                            d.add(f"{digits[i]}{digits[j]}{digits[k]}{digits[m]}")

        s = []
        for elem in d:
            for i in range(1, 4):
                s.append([elem[:i], elem[i:]])

        min_sum = int(s[0][0]) + int(s[0][1])
        for elem in s:
            if int(elem[0]) + int(elem[1]) < min_sum:
                min_sum = int(elem[0]) + int(elem[1])
        return min_sum