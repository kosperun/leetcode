class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date_arr = date.split("-")
        return "-".join([bin(int(i)).replace("0b", "") for i in date_arr])

        