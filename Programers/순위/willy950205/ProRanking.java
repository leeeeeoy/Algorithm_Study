package programmers;

public class ProRanking {
	public int solution(int n, int[][] results) {
        int answer = 0;
        
        // 어려웠던 점 : 초반에 플루이드 워셜 알고리즘을 인지하지 못하여
        // 헤매임. 자료를 찾아본 후에 해당 알고리즘이 필요하는 것을 인지함.
        // 이후 소장 중인 알고리즘 책을 다시 찾아보고 문제 풀이 성공
        
        // 주어진 results 배열 속 결과를 나열하는 배열선언
        boolean status [][] = new boolean [n][n];
        
        // results속의 결과를 기록한다. 이기는 경우 true로 바꾼다
        for(int [] arr : results) {
        	status[arr[0]-1][arr[1]-1] = true;
        }
        
        // 플루이드 워셜 알고리즘을 사용하여
        // 거처가는 정점(선수) 또한 표기해준다.
        for(int i=0; i<n; i++) {
        	for(int j=0; j<n; j++) {
        		for(int k=0; k<n; k++) {
        			if(status[j][i]&&status[i][k]) {
        				status[j][k] = true;
        			}
        		}
        	}
        }

        // 승패가 결정이 나있는 경우만 result를 1씩 카운트 한다.
        // result == n-1 인 경우 answer++ 한다.
        for(int i=0; i<n; i++){
            int result=0;
            for(int j=0; j<n; j++){
                if(status[i][j] || status[j][i]){result++;}
            }
            if(result==n-1){answer++;}
        }
        
        return answer;
    }
}
