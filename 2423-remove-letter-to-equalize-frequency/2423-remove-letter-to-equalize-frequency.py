class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = {}
        for el in word:
            letter_freq = word.count(el)
            if letter_freq in freq:
                freq[letter_freq].add(el)
            else:
                freq[letter_freq] = {el}
        if len(freq) > 2:
            return False
        if len(freq) == 1:
            if 1 in freq:
                return True
            for k, v in freq.items():
                if len(v) == 1:
                    return True
            # if 1 in freq or 2 in freq and len(freq[2]) == 1:
            #     return True
                return False
        if len(freq) == 2:
            if 1 in freq:
                if len(freq[1]) == 1:
                    return True
                if 2 in freq:
                    if len(freq[2]) == 1:
                        return True
            keys = [item for item in freq.keys()]
            for i in range(len(keys) - 1):
                if keys[i] > keys[i + 1]:
                    bigger, smaller = keys[i], keys[i + 1]
                else:
                    bigger, smaller = keys[i + 1], keys[i]
                if bigger - smaller != 1:
                    return False
                if len(freq[bigger]) == 1:
                    return True