package programmers;

public class Immigration {
	public long solution(int n, int[] times) {
		
		// 이분탐색을 활용하여 문제를 해결
		// 어려웠던 점 : 이분탐색 알고리즘은 쉽지만 해당문제에
		// 어떻게 적용해야 할지 몰라 자료를 찾아봄.
		// 그 결과 가장 오래걸리는 시간을 찾아서 그 시간부터 찾아가면 됨
		
		
        long answer = 0;
        long end =0;
        
        // 가장 오래 걸리는 시간을 찾기위한 반복문
        for(int time : times) {
        	if(time>=end) {
        		end = time;
        	}        	
        }
        // 가장 오래걸리는 입국심사자에게 모두 검사받았을 경우
        // 걸리는 시간 구하기
        end*=n;
        // 이분탐색 메소드 실행
        answer = binarySearchWhile(0, end, times, n);       
        
        
        return answer;
    }
	
	
	public long binarySearchWhile(long start, long end, int [] times, long n) {
		// 중간 값을 구하기 위한 변수 선언
		long mid = 0;		
		// 해당 중간 값에서 받을 수 있는 손님의 수를 세기위한 변수 선언
		long count=0;
		// 답
		long answer=0;
		while(start<=end) {
			// 중간 값
			mid = (start+end)/2;
			// 해당 중간 값 당 받을 수 있는 손님 수 초기화
			count=0;
			// 받을 수 있는 손님 수 카운트
			for(int time : times) {
				count+=(mid/time);
			}
			
			// 만약 받을 수 있는 손님 수가 실제로 온 손님 수와 같거나
			// 크면 중간 값을 mid-1로 바꾼다.
			if(count>=n) {
				
				// 만약 answer가 바뀐적이 없다면
				// answer값을 mid로 초기화 한다.
				if(answer==0) {
					answer=mid;
					
				// 그렇지 않다면 
				// answer값을 현재 answer값과 중간 값과
				// 비교하여 더 작은 값을 answer에 넣어 
				// 가장 적은 시간을 구하도록 한다.
				}else {
					answer = Long.min(mid, answer);
				}
				end = mid-1;
			}else if(count<n) {
				start = mid+1;
			}
			
		}
		
		return answer;
		
	}
}
