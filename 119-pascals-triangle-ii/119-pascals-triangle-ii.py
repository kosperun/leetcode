class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1]]
        while len(result) < rowIndex+1:
            temp_list = [1]
            last_el = result[-1]
            for i in range(len(last_el) - 1):
                temp_list.append(last_el[i] + last_el[i + 1])
            temp_list.append(1)
            result.append(temp_list)
        return result[rowIndex]
