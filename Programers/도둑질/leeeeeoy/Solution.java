public class Solution {
    int[][] dp = new int[10000001][2];

    public int solution(int[] money){
        dp[0][0] = money[0];
        dp[1][0] = Math.max(money[0], money[1]);

        for (int i = 2; i<money.length-1;i++){
            dp[i][0] = Math.max(dp[i-2][0]+money[i], dp[i-1][0]);
        }
        dp[1][1] = money[1];
        for (int i = 2; i < money.length; i++) {
            dp[i][1] = Math.max(dp[i-2][1]+money[i], dp[i-1][1]);
        }
        int answer = Math.max(dp[money.length-2][0], dp[money.length-1][1]);
        return answer;
    }
}