package practice;

public class Network {
	
	// node를 방문했는지 알기위한 boolea타입 배열
	boolean [] visited ;
	
	public int solution(int n, int[][] computers) {
        int answer = 0;
        
        visited = new boolean[n];
        
        // 모든 node를 방문하기 위한 반복문
        for(int node =0; node<n; node++) {
        
        	// 만약 해당 node를 방문하지 않았다면 방문
        	if(!visited[node]) {
        		answer++;
        		// 연결되어있는 다른 node들을 방문
        		dfs(n,node,computers,visited);
        	}
        	
        }
        
        return answer;
    }
	
	
	public void dfs(int n, int node, int[][] computers, boolean [] visited) {
		// 방문한 node를 표기
		visited[node]=true;
		
		// 방문한 해당 node에 연결된 모든 node에 방문하기 위한 반복문
		for(int i=0; i<n; i++) {
			
			// 만약 다른 노드에 이 노드가 연결되어 있고, computers[node][i]==1
			// 자기 자신이 아니며, i!=node
			// 방문한 적이 없다면 해당 노드에 방문하는 조건문, !visited[i]
			if(computers[node][i]==1&&i!=node&&!visited[i]) {
				// 연결된 node에 방문
				dfs(n,i,computers,visited);
			}
		}
	}
}
