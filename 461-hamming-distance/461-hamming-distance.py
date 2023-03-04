class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dif = 0
        small, big = (x, y) if x <= y else (y, x)
        x_bin = bin(small)[2:]
        y_bin = bin(big)[2:]
        x_bin = "0" * (len(y_bin) - len(x_bin)) + x_bin
        for i, el in enumerate(x_bin):
            if el != y_bin[i]:
                dif += 1
        return dif
