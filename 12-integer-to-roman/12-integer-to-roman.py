class Solution:
    def intToRoman(self, num: int) -> str:
        int_rom_map = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        map_reduce = {4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"}

        int_list = [1000, 500, 100, 50, 10, 5, 1]
        dim_list = [900, 400, 90, 40, 9, 4]

        s = ""
        for i, item in enumerate(int_list):
            if num >= item:
                s += (num//item)*int_rom_map[item]
                num = num % item
            if i < len(dim_list) and num >= dim_list[i]:
                s += map_reduce[dim_list[i]]
                num -= dim_list[i]
            continue
        return s
