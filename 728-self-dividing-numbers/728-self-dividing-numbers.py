class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        numbers_int = list(range(left, right + 1))
        res = []
        numbers = []
        for num in numbers_int:
            numbers.append(str(num))

        for num in numbers:
            digs = list(num)
            temp_cnt = 0
            for el in digs:
                if (
                    "0" not in num
                    and int(el) != 0
                    and int(num) % int(el) == 0
                ):
                    temp_cnt += 1
            if temp_cnt == len(num):
                res.append(int(num))
        return res

