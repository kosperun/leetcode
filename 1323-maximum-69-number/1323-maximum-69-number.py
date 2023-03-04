class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        dig_list = [dig for dig in str(num)]
        dig_modified = [num_str]
        for i in range(len(dig_list)):
            if dig_list[i] == "9":
                dig_modified.append(num_str[:i] + "6" + num_str[i + 1 :])
            if dig_list[i] == "6":
                dig_modified.append(num_str[:i] + "9" + num_str[i + 1 :])
        res = [int(elem) for elem in dig_modified]
        return max(res)

