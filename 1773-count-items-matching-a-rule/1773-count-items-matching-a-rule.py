class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        for elem in items:
            if any([ruleKey == 'type' and elem[0] == ruleValue, ruleKey == 'color' and elem[1] == ruleValue, ruleKey == 'name' and elem[2] == ruleValue]):
                cnt += 1
        return cnt