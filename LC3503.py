class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        result = 1
        if s == s[::-1]:
            result = len(s)
        if t == t[::-1]:
            result = max(result, len(t))
        for i in range(len(s)):
            for j in range(i , len(s)):
                
                stringOne = s[i:j+1]
                if stringOne == stringOne[::-1]:
                    result = max(result, len(stringOne))
        for i in range(len(t)):
            for j in range(i , len(t)):
                
                stringOne = t[i:j+1]
                if stringOne == stringOne[::-1]:
                    result = max(result, len(stringOne))
            
        for i in range(len(s)):
            for j in range(i , len(s)):
                stringOne = s[i:j+1]
        
                for m in range(len(t)):
                    for n in range(m , len(t)):
                        stringTwo = t[m:n+1]

                        final = stringOne + stringTwo



                        if final == final[::-1]:
                            result = max(result, len(final))
        return result