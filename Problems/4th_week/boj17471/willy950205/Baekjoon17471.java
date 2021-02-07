package baekjoon;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Baekjoon17471 {
	
	static int [] population;
	static List<Integer> graph [];
	static boolean visited [];
	static Map<Integer, Integer> map;
	static int answer;
	static int total;
	
	
	public static void main(String [] args) {
		
		Scanner scn = new Scanner(System.in);
		
		int N = scn.nextInt();
		int graphCnt=0;
		population = new int [N];
		graph = new ArrayList [N];
		map = new HashMap<Integer, Integer>();
		answer=Integer.MAX_VALUE;
		
		
		for(int i =0; i<N; i++) {
			population[i] = scn.nextInt();
		}
		
		for(int i=0; i<N; i++) {
			graph[i] = new ArrayList<Integer>();
		}
		
		for(int i=0; i<N; i++) {
			int a = scn.nextInt();
			for(int j=0; j<a; j++ ) {
				int b = scn.nextInt();
				graph[i].add(b-1);
			}
		}
		
		visited = new boolean[N];
		for(int i=0; i<N; i++) {
			if(!visited[i]) {
				graphCnt+=1;
				bfs(i,graphCnt);
			}
		}
		
		
		total=map.get(1);
		
		if(graphCnt>2) {
			System.out.println(-1);
			return;
		}else if(graphCnt==2){
			System.out.println(Math.abs(map.get(1)-map.get(2)));
		}else if(graphCnt==1) {
			
			for(int i=0; i<N; i++) {
				boolean [] gv = new boolean [N];
				gerrymandering(i,gv,0);
			}
			System.out.println(answer);
			
		}

		
	}
	
	public static void bfs(int node, int cnt) {
		
		visited[node] = true;
		map.put(cnt, map.getOrDefault(cnt, 0)+population[node]);

		for(int a : graph[node]) {
			if(!visited[a]) {
				bfs(a,cnt);
			}
		}
	}
	
	public static void gerrymandering(int node, boolean [] gv, int currPo) {
		
		gv[node]=true;
		currPo+=population[node];
		int diff = Math.abs(total-currPo-currPo)  ;
		answer=Integer.min(answer,diff);
		for(int a : graph[node]) {
			if(!gv[a]) {
				boolean [] gv2 = gv.clone();
				gerrymandering(a,gv2,currPo);
			}			
		}
	}
}
