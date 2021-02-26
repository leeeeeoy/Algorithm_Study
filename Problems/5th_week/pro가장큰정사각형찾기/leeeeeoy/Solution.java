public class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[][] case1 = {{0,1,1,1}, {1,1,1,1}, {1,1,1,1}, {0,0,1,0}};
        int[][] case2 = {{0,0,1,1},{1,1,1,1}};
        System.out.println(s.solution(case1));
        System.out.println(s.solution(case2));
    }
    public int solution(int [][]board) {
        int answer  = 0;
        int row = board[0].length;
        int col = board.length;
        int max = 0;

        if (row == 1 && col == 1){
            if (board[0][0] == 0)
                return 0;
            else if (board[0][0] == 1)
                return 1;
        }
        for (int i = 1; i < col; i++){
            for (int j = 1; j < row; j++){
                if (board[i][j] >= 1){
                    int u = board[i-1][j];
                    int l = board[i][j-1];
                    int ul = board[i-1][j-1];
                    int min = Math.min(u, Math.min(l, ul));
                    board[i][j] = min+1;
                    max = Math.max(max, min+1);
                }
            }
        }
        answer = max * max;
        return answer;
    }
}