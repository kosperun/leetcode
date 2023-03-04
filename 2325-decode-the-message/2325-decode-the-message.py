class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        s = list((chr(ord_) for ord_ in range(ord("a"), ord("{"))))
        s = "".join(s)
        key = key.replace(" ", "")
        new_key = ""
        for elem in key:
            if elem not in new_key:
                new_key += elem
        order = {}
        for elem in new_key:
            if elem not in order:
                order[elem] = s[new_key.index(elem)]
        order[" "] = " "
        res = ""
        for elem in message:
            res += order[elem]
        return res