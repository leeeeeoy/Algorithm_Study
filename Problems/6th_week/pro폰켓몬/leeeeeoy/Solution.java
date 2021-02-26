import java.util.HashSet;

public class Solution {
    public static void main(String[] args) {
        int[] case1 = {3,1,2,3};
        int[] case2 = {3,3,3,2,2,4};
        int[] case3 = {3,3,3,2,2,2};

        Solution s = new Solution();
        System.out.println(s.solution(case1));
        System.out.println(s.solution(case2));
        System.out.println(s.solution(case3));

    }
    public int solution(int[] nums) {
        int answer = 0;

        int max = nums.length/2;
        Set<Integer> mySet = new HashSet<>();
        for (int num : nums){
            mySet.add(num);
        }
        if (mySet.size() > max){
            answer = max;
        }else{
            answer = mySet.size();
        }
        return answer;
    }
}