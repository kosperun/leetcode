class Solution:
    def freqAlphabets(self, s: str) -> str:
        # Create mappings for a-i and j-z letters:
        a_i = [chr(i) for i in range(ord("a"), ord("i") + 1)]
        a_i_mapping = {str(k): a_i[k - 1] for k in range(1, 10)}
        j_z = [chr(i) for i in range(ord("j"), ord("z") + 1)]
        j_z_mapping = {str(k): j_z[k - 10] for k in range(10, 27)}
        # Get indexes of all # in s:
        inds = []
        for i, el in enumerate(s):
            if el == "#":
                inds.append(i)
        res = []
        start = 0
        # Convert all characters before the last # in s into their corresponding mappings:
        for i in inds:
            if i > 1:
                for j in range(start, i - 2):
                    res.append(a_i_mapping[s[j]])
            res.append(j_z_mapping[s[i - 2 : i]])
            start = i + 1
        # Convert the rest of s (after the last # symbol):
        if inds[-1] < len(s) - 1:
            for k in s[inds[-1] + 1 :]:
                res.append(a_i_mapping[k])
        fin = "".join(res)
        return fin
