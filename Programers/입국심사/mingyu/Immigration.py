"""
Programmers. 입국 심사
url: https://programmers.co.kr/learn/courses/30/lessons/43238
writer: Mingyu
Language: Python3
Date: 2021.01.29
Status: , Runtime:  ms, Memory Usage:  KB
"""


def solution(n, times):
    answer = 0

    # 검사의 범위를 설정한다.
    # 검사의 시작지점(left): 검사 시간이 가장 빠른 심사관부터 시작
    # 검사의 끝 지점(right): 최악의 경우. 검사 시간이 가장 긴 심사관이 모두를 검사하는 상황이 마지막 지점
    left, right = min(times), max(times) * n

    # 좌 우를 줄여가며 검사 범위를 좁힐 것이다. left > right가 되면 검사가 끝났다는 소리가 된다
    while(left <= right):

        # 중간 지점은 (시작+끝)//2이다. 소수점 배제를 위해 몫 연산으로 계산
        # 해당 중간 지점의 범위를 좁혀 가면서 최적의 시간을 찾는다.
        # 한 심사관에게 주어진 시간으로 활용할 것이며, 심사관이 한 명을 처리하는 데 걸리는 시간으로 나누어 몇 명을 처리할 수 있는지 확인할 것이다.
        mid = (left + right) // 2

        # 검사가 완료된 사람의 수.
        people = 0

        # 각 심사관을 돌면서
        for officer in times:

            # 주어진 시간 동안 몇 명의 사람을 검사할 수 있는지 확인
            people += mid // officer
            
            # 검사가 완료된 사람이 n보다 크다면 모든 사람을 검사하고도 주어진 시간이 남는다는 것이다.
            if people >= n:

                # 그러므로 mid를 answer에 저장한 후 조금 더 줄여서 다시 확인해본다.
                answer = mid

                # 주어진 시간이 남는 것이므로 최대 부분에서 -1을 한다.
                right = mid - 1

                # right 값을 변경하였으므로 현재 단계에서는 더이상 진행할 필요가 없다. 다음 단계로 가기 위해 해당 for문을 탈출.
                break

        # 위의 상황과 반대로 주어진 시간 내에 심사가 끝나지 않은 상황이다.
        if people < n:
            # 최소 시간이 부족하다는 뜻이므로 최소 시간에 +1을 해준다.
            left = mid + 1

    return answer



''' 주석 없는 코드
def solution(n, times):
    answer = 0
    left, right = min(times), max(times) * n

    while(left <= right):

        mid = (left + right) // 2
        people = 0

        for officer in times:
            people += mid // officer

            if people >= n:
                answer = mid
                right = mid - 1
                break

        if people < n:
            left = mid + 1

    return answer
'''