class Solution:
def longestBeautifulSubstring(self, word: str) -> int:
sub = ""
result = 0
i = 0
j = 0

v = "aeiou"
d= {}
        for i in range(1, len(v)):
d[v[i]] = v[i-1]
d['a'] = 'a'
i =0
prev = ''
        while j < len(word):
        if word[j] == "a":
prev = 'a'
j += 1
        while j < len(word):
current = word[j]
        if current != prev:
        if d[current] != prev:
        break
prev = current

j += 1
        # print(i , j , prev )
                if prev == 'u':
        # print("anguttu")
result = max(result , j - i )
i = j
            else:
j += 1
i = j
        # print(i , j , prev)
        if prev == 'u':
        # print("inguttu")
result = max(result , j - i)

        return result


