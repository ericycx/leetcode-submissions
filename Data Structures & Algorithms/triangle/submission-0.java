class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.get(triangle.size() -1).size();
        int[][] H = new int[n][n];
        H[0][0] = triangle.get(0).get(0);
        int i = 1;
        int j = 1;
        while (i < triangle.size()){
            H[i][0] = triangle.get(i).get(0) + H[i-1][0];
            H[i][i] = triangle.get(i).get(i) + H[i-1][i-1];
            while (j < triangle.get(i).size() - 1){
                H[i][j] = triangle.get(i).get(j) + Math.min(H[i-1][j-1], H[i-1][j]);
                j ++;
            }
            j = 1;
            i ++;
        }
        int m = Arrays.stream(H[n-1]).min().getAsInt();
        return m;
    }
}