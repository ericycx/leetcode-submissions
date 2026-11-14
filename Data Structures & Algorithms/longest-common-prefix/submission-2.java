class Solution {
    public String longestCommonPrefix(String[] strs) {
        String cur = strs[0];
        for (String s : strs) {
            int i = 0;
            while (i < cur.length() && i < s.length() && cur.charAt(i) == s.charAt(i)) {
                i++;
            }
            cur = cur.substring(0, i);
            if (cur.isEmpty()) break;
        }
        return cur;
    }
}