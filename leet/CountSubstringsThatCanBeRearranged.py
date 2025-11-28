from typing import Counter
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        i = 0
        j = 0
        d1= Counter(word2)
        d = Counter()
        result = 0
        current = 0
        l = len(word1)
        final = len(d1)
        while j < len(word1):
            d[word1[j]] += 1
            if word1[j] in d1 and d[word1[j]] == d1[word1[j]]:
                current += 1
            while current == final:
                result += l - j
                if word1[i] in d1 and d[word1[i]] == d1[word1[i]]:
                    current -= 1
                d[word1[i]] -= 1
                i += 1
                    
            j += 1
        return result
            
            