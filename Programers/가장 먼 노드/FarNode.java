package programmers;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class FarNode {
	public int solution(int n, int[][] edge) {
        int answer = 0;
        
        // 어려웠던 점 : 가장 먼 노드들의 수 구하는 것
        
        // bfs를 사용하였다.
        
        // 노드의 방문 여부 체크
        boolean visited [] = new boolean[n];
        
        // 방문하기 위한 노드를 담을 Queue 선언
        Queue<Integer> q= new LinkedList<Integer>();
        
        // edge 배열을 connection배열에 담는다. arrayList의 contanins 메소드를 사용하여
        // 연결 여부를 확인하기 위해
        ArrayList<Integer> connection [] = new ArrayList[n] ;
        
        // 각 노드들의 거리를 기록하기 위한 배열
        int [] nodeDis = new int [n];
        // 가장 먼 노드의 거리를 체크하기 위한 선언
        int mostFar =0;
        
        // 각 배열에 ArrayList 생성
        for(int i=0; i<n; i++) {
        	connection[i] = new ArrayList<Integer>();
        }
        
        // edge 배열의 연결을 connection으로 넣어준다.
        for(int i=0; i<edge.length; i++) {
        	int x = edge[i][0]-1;
        	int y = edge[i][1]-1;
        	
        	connection[x].add(y);
        	connection[y].add(x);        	
        }
        
        q.add(0);
        visited[0]=true;
        
        //bfs 구현부
        while(!q.isEmpty()) {
        	int node = q.poll();
        	for(int j=0; j<n; j++) {
        		if(connection[j].contains(node)&&!visited[j]) {
        			nodeDis[j] = nodeDis[node]+1;
        			visited[j] = true;
        			q.add(j);     
        			mostFar = Integer.max(mostFar, nodeDis[j]);
        			
        		}
        		
        	}      	
       	}
        
        
        for(int i=0; i< n; i++) {
        	if(nodeDis[i]==mostFar) {
        		answer++;
        	}
        }
        
               
        return answer;
    }
	
}