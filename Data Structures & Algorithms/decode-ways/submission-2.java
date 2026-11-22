class Solution {
    public int numDecodings(String s) {
        if (s.charAt(0) == '0') {
            return 0;
        }
        List<Integer> H = new ArrayList<>();
        H.add(1);
        for (int i = 1; i < s.length(); i++) {
            int ways = 0;
            if (s.charAt(i) != '0') {
                ways += H.get(i - 1);
            }
            // previous + current as a two-digit letter
            int two = (s.charAt(i - 1) - '0') * 10 + (s.charAt(i) - '0');
            if (two >= 10 && two <= 26) {
                ways += (i >= 2) ? H.get(i - 2) : 1;
            }
            H.add(ways);
        }
        return H.get(s.length() - 1);
    }
}