"""
Programmers. 여행경로
url: https://programmers.co.kr/learn/courses/30/lessons/43164
writer: Mingyu
Language: Python3
Date: 2021.02.16
Status: , Runtime:  ms, Memory Usage:  KB
"""

def solution(tickets):
    # 항공권 정보를 딕셔너리로 설정
    route = dict()
    
    # a도시에서 b도시로 가는 경로를 딕셔너리에 추가
    for a, b in tickets:
        if a not in route:
            route[a] = [b]
        else:
            route[a].append(b)

    # 스택을 사용할 것이기 때문에 도착지(b도시)를 역순으로 정렬해둔다.
    for i in route:
        route[i].sort(reverse=True)
            
    # 처음 방문할 도시는 반드시 ICN이며, 여기에 방문해야 할 도시들을 추가해 나갈 것이다.
    need_visit = ["ICN"]

    # 정답을 저장할 배열
    answer = []

    # 더 이상 방문할 도시가 없을 때까지
    while need_visit:
        # 방문해야 할 도시들 중 가장 마지막에 있는 도시를 다음 도시로 설정
        # 밑의 else문에서 다음 방문해야 할 도시를 계속 추가해 줄 것이기 때문이다.
        cur_city = need_visit[-1]

        # 해당 도시에서 출발하는 경우가 없거나 해당 도시에서 가야 할 도착지를 전부 돌았다면
        if cur_city not in route or len(route[cur_city]) ==0:
            # 해당 도시를 answer에 추가
            answer.append(need_visit.pop())
        
        # 다음에 가야 할 도시가 있다면
        else:
            # 현재 도시와 연결된 도착지 중 마지막 것을 다음에 방문할 도시로 설정
            # 이를 위해 위에서 역순으로 정렬하였다. 역순으로 정렬했으므로 마지막 것이 알파벳이 제일 작은 것(순서가 앞서는 것)이다.
            need_visit.append(route[cur_city].pop())
        
    # 스택으로 구현했기 때문에 answer에는 역순으로 들어가있다. 이를 반대로 뒤집으면 된다.
    answer.reverse() 
    return answer



''' 주석 없는 코드

def solution(tickets):
    route = dict()
    
    for a, b in tickets:
        if a not in route:
            route[a] = [b]
        else:
            route[a].append(b)

    for i in route:
        route[i].sort(reverse=True)
            
    need_visit = ["ICN"]
    answer = []

    while need_visit:
        cur_city = need_visit[-1]

        if cur_city not in route or len(route[cur_city]) ==0:
            answer.append(need_visit.pop())
        else:
            need_visit.append(route[cur_city][-1])
            route[cur_city].pop()

    answer.reverse()
        
    return answer
'''