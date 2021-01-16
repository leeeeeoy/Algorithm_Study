package practice;

public class ProThievery {
    public int solution(int[] money) {

        int answer =0;

        // 첫번째 집을 무조건 턴 후의 동적계획법 배열 결과
        int [] result = new int[money.length];
        // 마지막 집을 무조건 턴 후의 동적계획법 배열 결과
        int [] result2 = new int[money.length];


        // 첫번째 집을 무조건 터는 반복문
        for(int i=0; i<money.length; i++){

            // 첫번째 집을 무조건 털어 result배열의 첫번째 값에 money[0]의 값을 넣어준다.
            if(i==0){
                result[i]=money[0];

                // 첫번째 집을 무조건 털었기 때문에 두번째 집은 털수 없다. 그래서
                // 첫번째 집과 동일한 값을 갖는다.
            }else if(i==1){
                result[i] = money[0];


                // 첫번째 집을 털었고 집들의 순서가 원형으로 구성되어있기 때문에
                // 구조상 첫번째 집과 마지막 집이 서로 이웃한다.
                // 이러한 사실을 고려하면 마지막 집은 털수 없다. 그렇기 때문에
                // 마지막 집의 result값은 이전의 result값과 동일하다.
            }else if(i==money.length-1) {
                result[i] = result[i-1];


                // 첫번째 집과 두번째 집 이후의 집에대해서는
                // 방범 장치를 고려하여 가질 수 있는 최댓값을 result[i]값에 넣어준다.
            }else {
                result[i] = Integer.max(result[i-2]+money[i],result[i-1]);
            }
        }

        // 마지막을 무조건 터는 반복문
        for(int i=1; i<money.length; i++){

            // 마지막 집을 턴다고 가정하기 때문에 첫번째 집은 털수 없다.
            // 그렇기 때문에 result2값을 0을 넣어준다.
            if(i==0){
                result2[i]=0;

                // 첫번째 집을 털지 않았기 때문에 두번째 집은 털수 있다.
                // 그렇기 때문에 result2값에 money[1] 값을 넣어준다.
            }else if (i==1) {
                result2[i] = money[1];


                // 그 이후의 result2 값에 대해서는
                // 방범 장치를 고려하여 가질 수 있는 최댓값을 result2[i]값에 넣어준다.
            }else {
                result2[i] = Integer.max(result2[i-2]+money[i],result2[i-1]);
            }
        }

        // 첫번째 집을 무조건 털었을 때와
        // 마지막 집을 무조건 털었을 때의 배열의 최댓값을 비교하여
        // 더 큰 값을 answer에 넣어준다.
        answer = Integer.max(result[money.length-1],result2[money.length-1]);

        // answer를 return한다.
        // commit test
        return answer;

    }

}
