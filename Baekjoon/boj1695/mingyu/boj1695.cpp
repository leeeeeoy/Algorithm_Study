#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

// 입력받은 수열을 넣을 배열. 수열의 길이가 최대 5000이기 때문에 전부 최대 크기를 5000으로 설정하였다.
int arr[5000];

// 시작값과 끝 값을 비교할 동적계획 테이블. main함수에서 -1로 초기화할 예정이다.
int dp[5000][5000];

// 팰린드롬 함수. 재귀적으로 사용된다. 인자는 수열의 시작값과 끝 값을 의미한다.
int palindrome(int start, int end) {
	
	// 시작값이 끝 값보다 크다는 것은 더 이상 검사할 수열이 남아있지 않다는 것이다. 방어코드로 사용하였다.
	if (start > end)
		return 0;

	// result 변수를 생성해서 dp테이블에 포인터를 연결한다.
	int& result = dp[start][end];
	
	// dp테이블은 -1로 초기화된 상태이다. 즉 -1이면 처리해야 할 상태이고, -1이 아니라면 처리된 상태라는 뜻이 된다.
	// result가 처리되었다면(-1이 아니라면), 다시 처리할 필요가 없으니 result를 그대로 반환해주면 된다.
	if (result != -1) return result;

	// 수열에서 시작값과 끝 값이 같다는 것은 짝을 이룬다는 뜻이 된다. 즉 팰린드롬의 조건을 만족한다는 뜻이 된다.
	if (arr[start] == arr[end])
		// 짝을 이루고 있으니 수열의 앞뒤를 한 칸씩 줄여주면 다음 값들이 짝을 이루는지 검사할 수 있다. 
		result = palindrome(start + 1, end - 1);

	// 팰린드롬의 조건을 만족하지 않는 상태이다.
	// 양쪽의 경우를 비교해 보고, 삽입 횟수가 더 적은(효율적인) 부분을 선택한다.
	else
		// 시작 쪽이 삽입 횟수가 더 적다면 시작값에 +1을 해준다. 이후 해주는 +1은 start에 +1을 해서 배열의 크기가 1 줄어들었기 때문에 이를 보완해주는 역할을 한다.
		// 끝 쪽이 삽입 횟수가 더 적은 경우에도 마찬가지이다.
		result = min(palindrome(start + 1, end) + 1, palindrome(start, end - 1) + 1);

	
	return result;
}

int main() {
	int N;
	cin >> N;

	for (int i = 0; i < N; i++)
		cin >> arr[i];

	// dp 테이블을 -1로 초기화한다.
	memset(dp, -1, sizeof(dp));

	// 인자를 넣을 때, 0부터 시작하므로 수열의 길이 -1을 해주면 된다.
	cout << palindrome(0, N - 1) << endl;
	return 0;
	
}
