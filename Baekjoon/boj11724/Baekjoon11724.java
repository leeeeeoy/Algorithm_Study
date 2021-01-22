package baekjoon;

import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;

public class Baekjoon11724 {
	public static void main(String [] args) throws IOException {

		// dfs로 해결
		// 어려웠던 점 : 재귀를 사용하지 않고 구현하기 위해 고민. 가장 상위의 반복문 구현이 조금 헷갈림
		
		Scanner sc = new Scanner(System.in); 
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		int answer =0;
		
		// node 방문여부 확인을 위한 boolean 배열 선언
		boolean visited[] = new boolean[N];
		// 연결된 node 확인을 위한 이중 int 배열 선언 
		int graph [][] = new int [N][N];
		// dfs 구현을 위한 Stack 선언
		Stack<Integer> stack = new Stack<Integer>();
		
		// 입력과 동시에 graph 배열 채우기
		int a,b;
		for(int i = 0; i < M; i++) {
			a = sc.nextInt();
			b = sc.nextInt();	
			
			graph[a-1][b-1]=1;
			graph[b-1][a-1]=1;
		}

		
		// dfs 구현부
		for(int j=0; j<N; j++) {
			if(!visited[j]) {
				answer++;
				visited[j] = true;
				stack.add(j);
				
				while(!stack.isEmpty()) {
					int node = stack.pop();
					for(int i=0; i<N; i++) {
						if(graph[node][i]==1&&!visited[i]) {
							visited[i] =true;
							stack.add(i);
						}
					}
				}
			}
		}
		
		
		System.out.println(answer);
		
	}
}
