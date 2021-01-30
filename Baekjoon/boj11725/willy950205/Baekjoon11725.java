package baekjoon;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Baekjoon11725 {
	public static void main(String args []) {
		
		// bfs를 사용하여 문제 해결
		// 어려웠던 점 : 없음
		
		
		Scanner scn = new Scanner(System.in);
		// 노드의 개수 입력
		int N = scn.nextInt();
		
		// 트리를 인접 리스트로 구현하기 위한 list 선언
		List<Integer> list [] = new  ArrayList[N] ;
		// bfs를 구현하기 위한 큐 선언
		Queue<Integer> q = new LinkedList<Integer>();
		// 각 노드들의 부모 노드를 기록하기 위한 정수 리스트 선언
		int [] answer = new int [N];
		// 각 노드의 방문여부를 확인하기 위한 boolean 배열 선언
		boolean visited [] = new boolean [N] ;
		
		// 인접행렬 구현을 위한 각 인덱스에 ArrayList 생성
		for(int i=0; i<N; i++ ) {
			list[i] = new ArrayList<Integer>();
		}
		
		// 인접리스트 구현
		for(int i=0; i<N-1; i++) {
			int a = scn.nextInt()-1;
			int b = scn.nextInt()-1;
			
			list[a].add(b);
			list[b].add(a);
		}
		
		// 루트를 가장 처음으로 q에 넣음
		q.add(0);
		visited[0] = true;
		
		// bfs 구현부
		while(!q.isEmpty()) {
			int parentNode = q.poll();
			for(int childNode : list[parentNode]) {
				if(!visited[childNode]) {
					visited[childNode]=true;
					answer[childNode] = parentNode;
					q.add(childNode);
				}
				
			}
		}		
		
		// 답변 출력부
		for(int i=0; i<answer.length; i++) {
			if(i!=0) {
				System.out.println(answer[i]+1);
			}
			
		}
		
	}
}








