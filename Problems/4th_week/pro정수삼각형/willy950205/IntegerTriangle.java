package programmers;

public class IntegerTriangle {
	public int solution(int[][] triangle) {
		
		// 접근 방법 : dp사용
		// 정수형 이중 배열을 사용하여 각 층, 각 정수에 최대값을 기록하며 최대값을 
		// 찾았다.
		
		// 어려웠던 점 : 없음
		
        int answer = 0;
        
        int [][] result  = new int [triangle.length][triangle.length];
        
        result[0][0]=triangle[0][0];
        
        for(int i=1; i<triangle.length; i++) {
        	for(int j=0; j<triangle[i].length; j++) {
        		if(j==0) {
        			result[i][j]=result[i-1][j]+triangle[i][j];
        		}else if (j==triangle[i].length-1) {
        			result[i][j]=result[i-1][j-1]+triangle[i][j];
				}else {
					result[i][j]=Integer.max(result[i-1][j-1]+triangle[i][j], result[i-1][j]+triangle[i][j]);
				}
        		
        		answer = Integer.max(answer, result[i][j]);
        	}
        }
        
        
        
        return answer;
    }
}
