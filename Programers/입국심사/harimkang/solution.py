"""
Programmers 43238. 입국심사
url: https://programmers.co.kr/learn/courses/30/lessons/43238
writer: Harim Kang
Language: Python3
Date: 2021.01.29
Status: Success
정확성: 100.0
합계: 100.0 / 100.0
"""

def solution(n, times):
    answer = 0

    left = 1
    
    # 가능한 최대값
    right = (len(times) + 1) * max(times)

    while left <= right:
        mid = (left + right) // 2

        count = 0
        for time in times:
            count += mid // time
            # 심사 인원수를 넘으면 다음 단계
            if count >= n:
                break

        # n명을 심사 할 수 있는 경우
        if count >= n:
            answer = mid
            right = mid - 1
        # 없는 경우
        elif count < n:
            left = mid + 1

    return answer



if __name__ == "__main__":
    inputs = [
        [6, [7, 10]],
    ]
    expected = [28]
    resp = []
    for n, time in inputs:
        ans = solution(n, time)
        resp.append(ans)

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)