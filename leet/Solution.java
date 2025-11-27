public class Solution {
    public int longestBeautifulSubstring(String word) {
        int result = 0;
        int i = 0, j = 0;
        String vowels = "aeiou";
        char prev = '\0';

        while (j < word.length()) {
            if (word.charAt(j) == 'a') {
                prev = 'a';
                j++;

                while (j < word.length()) {
                    char current = word.charAt(j);
                    if (current != prev) {
                        if (vowels.indexOf(current) != vowels.indexOf(prev) + 1) {
                            break;
                        }
                    }
                    prev = current;
                    j++;
                }
                if (prev == 'u') {
                    result = Math.max(result, j - i);
                }
                i = j;
            } else {
                j++;
                i = j;
            }
        }
        return result;
    }
}