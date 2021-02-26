import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        double[] s = new double[N+1];
        for(int i : stages){
            if(i == N+1)
                continue;
            s[i]++;
        }
        ArrayList<Double> fail = new ArrayList<Double>();
        double num =stages.length;
        double tmp = 0;

        for(int i=1; i<s.length; i++){
            tmp = s[i];
            if(num == 0){
                s[i]=0;
            }else{
                s[i] = s[i]/num;
                num = num - tmp;
            }
            fail.add(s[i]);
        }
        Collections.sort(fail,Collections.reverseOrder());
        for(int i=0; i<fail.size(); i++){
            for(int j=1; j<s.length; j++){
                if(fail.get(i) == s[j]){
                    answer[i] = j;
                    s[j] = -1;
                    break;
                }
            }
        }
        return answer;
    }
}