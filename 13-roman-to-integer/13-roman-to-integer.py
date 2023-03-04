class Solution:
    def romanToInt(self, s: str) -> int:
        rom_int_map = {"I":1, "V":5, "X":10, "L":50, "C": 100, "D":500, "M":1000}
        dim_map = {"I": ["V", "X"], "X":["L", "C"], "C": ["D", "M"]}
        length = len(s)
        total= 0
        for i in range(length):
            char = s[i]
            if char in dim_map and i < length-1 and s[i+1] in dim_map[char]:
                total -= rom_int_map[char]
            else:
                total += rom_int_map[char]
        return total
            
        