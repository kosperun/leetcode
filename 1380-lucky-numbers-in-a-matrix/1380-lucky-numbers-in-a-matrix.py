class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        magic_numbers = []
        for row1 in matrix:
            min_num = min(row1)
            min_num_ind = row1.index(min_num)
            col_with_max_nums = []
            for row2 in matrix:
                col_with_max_nums.append(row2[min_num_ind])
            if min_num == max(col_with_max_nums):
                magic_numbers.append(min_num)
        return magic_numbers  