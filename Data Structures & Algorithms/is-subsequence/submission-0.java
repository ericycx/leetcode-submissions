class Solution {
    public boolean isSubsequence(String s, String t) {
        int n = 0;
        int m = 0;
        while (n < t.length() && m < s.length()){
            if (s.charAt(m) == t.charAt(n)){
                m += 1;
            }
            n += 1;
            System.out.println(n);
            System.out.println(m);
        }
        return m == s.length();
    }
}