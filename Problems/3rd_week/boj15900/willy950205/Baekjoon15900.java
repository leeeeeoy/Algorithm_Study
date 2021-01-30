package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Baekjoon15900 {
	
	// 각 노드의 방문여부를 확인하는 boolean 배열을 선언. 재귀적으로 dfs를 구현하기 위해 전역변수로 선언
	static boolean visited [];
	// 인접리스트로 tree를 구현하기 위한 list 배열 선언. 재귀적으로 dfs를 구현하기 위해 전역변수로 선언
	static List<Integer> tree [];
	// 말의 총 이동 횟수를 저장하기 위한 변수
	static int answer;
	
	public static void main(String args []) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// dfs를 이용하여 해결함
		// 어려웠던 점 : 처음엔 dfs를 재귀적 방법을 사용하지 않고 stack을
		// 사용하여 구현하려 하였으나 리프노드의 depth를 구하는 것에 실패하여
		// 재귀로 구현 후 성공. stack을 사용하여 구하는 방법이 있을까?
		
		int N = Integer.parseInt(br.readLine());
		
		// 전역변수 생성
		answer=0;
		visited = new boolean [N];
		tree = new ArrayList[N];

		// tree 각 인덱스 생성
		for(int i =0; i<N; i++) {
			tree[i] = new ArrayList<Integer>();
		}
	
		// 입력과 동시에 인접리스트 구현부
		for(int i=0; i<N-1; i++) {
			String input = br.readLine();
				
			// 인접리스트 구현부
			tree[Integer.parseInt(input.split(" ")[0])-1].add(Integer.parseInt(input.split(" ")[1])-1);
			tree[Integer.parseInt(input.split(" ")[1])-1].add(Integer.parseInt(input.split(" ")[0])-1);
		}
		
		// dfs 사용
		dfs(0,0);
		
		// 말의 총 이동 횟수가 홀수면 승리, 그렇지 못하면 패배
		if(answer%2==1) {
			System.out.println("Yes");
		}else {
			System.out.println("No");
		}	
			
	}
	
	
	
	static public void dfs(int node, int depth) {
		// 해당 노드 방문 체크
		visited[node] = true;
		
		// 각 노드 방문과 동시에 depth를 추가
		for(int child : tree[node]) {
			if(!visited[child]) {
				dfs(child, depth+1);
			}
		}
		
		// 만약 어떤 노드가 루트노드가 아닌데, 연결되어있는 노드가
		// 하나 뿐이라면 해당 노드는 리프노드이다.
		// 해당 노드가 리프노드면 answer에 depth를 더해준다.
		if(node!=0&&tree[node].size()==1) {
			answer+=depth;
		}
		
		
	}
}