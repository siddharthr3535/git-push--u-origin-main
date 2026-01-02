class Solution {
    public int minimumRecolors(String blocks, int k) {
        int result = blocks.length() + 1;
        int l = 0;
        int r = 0;
        int count = 0;

        while (r < blocks.length()) {
            if (blocks.charAt(r) == 'W') {
                count++;
            }
            if (r - l + 1 == k) {
                result = Math.min(result, count);
                if (blocks.charAt(l) == 'W') {
                    count--;
                }
                l++;
            }
            r++;
        }
        return result;
    }
}