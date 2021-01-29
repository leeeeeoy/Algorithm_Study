#include <iostream>
#include <string>

// a, b 둘 중 큰 값을 반환하는 함수
#define max(a, b) (a > b) ? a : b

using namespace std;

// DNA_dp[i][j] : i부터 j 인덱스의 문자열에서 KOI 유전자 길이가 저장된 배열
// 지역변수로 선언시 스택 크기를 감당하지 못해서 코드가 터진다. 설정하는 방법이 있다고는 하는데 전역변수로 처리하면 그냥 돼서 전역변수로 사용.
int DNA_dp[502][502];


int main() {
	string str;
	cin >> str;
	// 문자열의 길이
	int len = str.size();
	
	// size가 1부터 시작하는 이유는, 하단의 for문이 0부터 시작하기 때문이다. 
	// 동적계획법의 목적에 맞게, 가장 작은 단위부터 문자열이 조건을 성립하는지 확인해야 한다.
	// 조건 1에 따라, at 또는 gc가 가장 짧은 길이의 문자열이고, 이 문자열의 길이는 2이다.
	for (int size = 1; size < len; size++) {

		// start + size를 통해 검사할 문자열의 길이를 제한한다
		// 문자열 전체를 검사하는 것이 아니라, 문자열을 잘게 나누어 계속 확인하는 부분이다.
		for (int start = 0; start + size < len; start++) {

			// 검사할 문자열의 마지막 인덱스. 처음엔 end가 1이기 때문에 문자를 2개씩 확인하겠다는 것을 알수 있다.
			// 이후 3, 4, ... 순으로 검사하는 문자열의 마지막 인덱스가 점점 늘어난다.
			int end = start + size;

			// 조건 1, 2에 따라서, a와 t를 양 극단으로 갖거나 g와 c를 양 극단으로 가져야 한다.
			if ((str[start] == 'a' && str[end] == 't') || (str[start] == 'g' && str[end] == 'c'))
				
				// +2를 하는 이유는, 양 극단에 a,t 또는 g,c가 있다는 뜻이며  (두 개의 문자가 조건을 성립함, +2)
				// DNA_dp[start + 1][end - 1]의 값을 구하는 이유는 조건 2를 따르기 때문이다. 
				// 양 극단에 a, t 또는 g, c를 가지고 있는데, 그 안에 이미 조건 1을 만족하여 성립된 숫자가 있다면 그것 또한 더해준다는 뜻이다.
				DNA_dp[start][end] = DNA_dp[start + 1][end - 1] + 2;

			// 조건 3에 따라서, 어떤 X(DNA_dp[start][mid])와 Y(DNA_dp[mid + 1][end])가 KOI 유전자라면
			// 이 둘을 연결한(합친) 것도 KOI 유전자이다.
			for (int mid = start; mid < end; mid++) {

				// 앞부분과 뒷부분의 문자열을 더한 값을 v에 저장
				int v = DNA_dp[start][mid] + DNA_dp[mid + 1][end];
				
				// 해당 값(v)이 이전에 성립된 문자열의 길이(DNA_dp[start][end])보다 크다면 해당 값으로 변경
				DNA_dp[start][end] = max(DNA_dp[start][end], v);
			}
		}
	}
	
	// 0부터 위의 조건들이 성립된 마지막 문자열까지의 길이를 출력
	cout << DNA_dp[0][len - 1];
}
