package leetcode;


public class LeetCode55 {
	public boolean canJump(int[] nums) {
		
		// 접근방법 : 모든 가능성을 생각해보려 하였다.
		// nums의 모든 인덱스 마다 전진 가능한 index를 확인하면서
		// 진행하였다. 탐욕법을 사용했다고 보면 될거같음
		// 어려웠던점 : 처음에 방향그래프 문제라고 생각해서
		// 조금 헤맸다.
		
		// 현 index에서 전진할 수 있는 index를 기록한다.
		int capability=0;
		boolean answer=false;
		
		// 모든 index를 확인한다.
		for(int i=0;i<nums.length-1;i++) {
			// 모든 index를 확인하면서 더욱 전진할  수 있는지 확인하는 조건문이다.
			if(capability>=i) {
				// 전진할 수 있는 index를 갱신한다.
				capability=Integer.max(capability, i+nums[i]);
				// 만약 마지막 index까지 전진할 수 있는 index를 발견하면 더이상
				// 확인하지 않고 반복문을 탈출한다.
				if(capability==nums.length-1) {
					break;
				}
			}
			
		}
		// 전진가능한 인덱스가 마지막 인덱스와 같다면 answer를 true로
		// 바꾼다.
		if(capability==nums.length-1) {
			answer=true;
		}

		return answer;
    }
	
	
}
