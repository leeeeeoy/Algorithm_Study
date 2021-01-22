package baekjoon;

import java.util.Scanner;

public class Baekjoon1753 {
	public static void main(String args[]) {
		Scanner scn = new Scanner(System.in);
		
		// 플루이드 워셀 알고리즘 사용
		// 실패원인 : 메모리 초과
		
		int V = scn.nextInt();
		int E = scn.nextInt();
		
		int startNode = scn.nextInt()-1;
		
		int graph [][] = new int [V][V];
		
		for(int i=0; i<V; i++) {
			for(int j=0; j<V; j++) {
				graph[i][j]= 20;
			}

		}
		

		for(int i=0; i< E; i++) {
			int a = scn.nextInt();
			int b = scn.nextInt();
			int c = scn.nextInt();
			
			graph[a-1][b-1] = c;
		}
		

		for(int i=0; i< V; i++) {
			for(int j =0; j<V; j++) {
				for(int k =0; k<V; k++) {
					graph[j][k] = Integer.min(graph[j][i]+graph[i][k], graph[j][k]); 
				}
			}
		}
		
		for(int i=0; i<V; i++) {
			if(i==startNode) {
				System.out.println(0);
			}else if(graph[startNode][i]==20) {
				System.out.println("INF");
			}else {
				System.out.println(graph[startNode][i]);
			}
		}
	}
}
