from typing import Counter


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        i = 0
        j = 0
        d1= Counter(word2)
        d = {}
        result = 0
        while j < len(word1):
            if word1[j] not in d:
                d[word1[j]] = 1
            else:
                d[word1[j]] += 1
            valid = True
            while valid:
                for k in d1:
                    if k not in d or d[k] < d1[k]:
                        valid = False
                        break
                if valid == True:
                    result += len(word1) - j 
                    d[word1[i]] -= 1
                    i += 1
            j += 1
        return result
            
            