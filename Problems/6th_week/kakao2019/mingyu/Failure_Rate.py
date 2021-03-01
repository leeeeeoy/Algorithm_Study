"""
Programmers. 실패율
url: https://programmers.co.kr/learn/courses/30/lessons/42889
writer: Mingyu
Language: Python3
Date: 2021.02.23
Status: , Runtime:  ms, Memory Usage:  KB
"""


def solution(N, stages):

    # 도전자의 수는 stages의 길이와 같다.
    challengers = len(stages)

    # 각 스테이지에서의 실패율을 저장할 배열
    failures = list()

    # 스테이지의 수만큼 돌 것이다.
    #  1 ~ N+1의 범위로 도는 이유는 마지막 스테이지까지 클리어한 사용자 (N+1)을 배열에 담기 위함이다.
    for i in range(1, N+1):
        # 밑에서 stages.count(i) / challengers의 식을 수행하게 될건데, stages.count(i)를 0으로 나눌 수는 없으므로
        # 0이하가 되는 것은 stages.count(i)가 그대로 나오기 위해 1로 나누는 것으로 설정
        if challengers <= 0:
            challengers = 1

        # (현재 스테이지를 아직 깨지 못한 사람 / 이전 스테이지는 깼으나 현재 스테이지부터 마지막 스테이지까지 깨지 못한 도전자)
        failures.append(stages.count(i) / challengers)
        # 다음 스테이지로 넘어갈 때 현재 스테이지에 남아있는 사람들은 빼준다.
        challengers -= stages.count(i)

    # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호를 출력해야 한다.
    # enumerate를 사용하여 스테이지에 번호를 부여한다. start = 1을 사용하여 시작 번호를 1로 설정
    # 현재 failures 는 (스테이지 번호, 실패율)의 상태로 저장되어 있다.
    # key=lambda x: x[1]를 사용하여 실패율을 기준으로 reversed = True, 내림차순으로 정렬한다.
    failures = sorted(enumerate(failures, start=1),
                      key=lambda x: x[1], reverse=True)

    # 실패율을 기준으로 내림차순 정렬된 failures에서 스테이지 번호만 뽑아 list화 하여 return
    return [i[0] for i in failures]


''' 주석 없는 코드

def solution(N, stages):

    challengers = len(stages)
    failures = list()

    for i in range(1, N+1):
        if challengers <= 0:
            challengers = 1
    
        failures.append(stages.count(i) / challengers)
        challengers -= stages.count(i)

    failures = sorted(enumerate(failures, start=1),
                      key=lambda x: x[1], reverse=True)

    return [i[0] for i in failures]
'''
