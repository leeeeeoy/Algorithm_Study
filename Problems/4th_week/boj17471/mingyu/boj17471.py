"""
Baekjoon 17471. 게리맨더링
url: https://www.acmicpc.net/problem/17471
writer: Mingyu
Language: Python3
Date: 2021.01.31
Status: , Runtime:  ms, Memory Usage:  KB
"""

import sys

# sys.stdin.readline를 계속 쓰기 싫어서 변수로 대체. 처음에 read에 sys.stdin.readline()로 ()까지 다 붙여서 써서 오류가 났다.
read = sys.stdin.readline

# 구역의 개수
N = int(read())

# 각 구역의 인구 수. 구역 번호가 1부터 시작하기 때문에 인덱스를 맞추기 위해 [0] + ~ 형식으로 작성하였다.
population = [0] + list(map(int, read().split()))

# 도시의 생김새를 따른 그래프를 그릴 딕셔너리 생성
city = dict()

# 도시 번호는 1부터 시작하기 때문에 (1, N+1)만큼 돈다.
for i in range(1, N+1):
    # 입력을 전부 받으면서, 첫 번째 입력은 단순히 인접한 구역의 수를 나타내는 것이기 때문에 [1:]을 사용하여 잘라낸다.
    city[i] = list(map(int, read().split()))[1:]

# 비트마스킹. 비트 연산을 사용하여 모든 부분집합을 구한다.
# https://blog.naver.com/kmh03214/221702095617 룰 참고하였다.
# set은 모든 부분집합을 구할 모집합
def powerset(set):

    # 비트연산에 사용할 마스크. len(set)에 따라 [1, 2, 4, 8, 16, ..]이 된다.
    masks = [1 << i for i in range(len(set))]

    # 1 << len(set)은 pow(2, len(set))과 같다. pow(2, len(set))은 set의 총 부분집합의 개수이다.
    for i in range(1 << len(set)):
        # 제너레이터는 한 번 실행될 때마다 yield를 반환한다.
        # 여기에서 반환하는 것은 [선택한 도시들의 집합], [선택하지 않은 도시들의 집합] 이다.
        yield [element for mask, element in zip(masks, set) if mask & i], [element for mask, element in zip(masks, set) if mask & (-i-1)]


# 선택한 도시 잡합의 시작점(첫 번째 부분집합)과 선택하지 않은 도시의 전체(두 번째 부분집합)를 인자로 받는다.
# 이 두 부분집합이 모두 연결그래프인지 알기 위해 bfs를 사용한다.
# 선택하지 않은 도시들을 모두 방문한 상태로 표시한 후, 선택한 도시 집합을 확인하면서 연결 그래프를 그렸을 때
# 전체 집합인 city와 길이가 같아지면 모두 연결되었다고 볼 수 있다.
def bfs(start, unselected_citys):
    
    # 선택하지 않은 도시들을 모두 방문한 상태로 표시
    visited = {i: 1 for i in unselected_citys}    

    # 선택한 도시들을 방문하기 위해 시작점을 방문 딕셔너리에 추가
    visited[start] = 1   

    # 선택된 도시들을 돌 것이며, 이를 위해 선택된 도시의 시작점을 인자에서 받아와 지정함
    selected_citys = [start]

    # 선택한 도시들을 하나씩 돌면서
    for v in selected_citys:

        # 해당 도시와 연결된 인접 도시들을 확인한다.
        for u in city[v]:

            # 인접 도시를 확인했을 때 아직 방문하지 않은 도시라면
            if u not in visited:
                
                # 방문함으로 표시한 후
                visited[u] = 1
                
                # 선택한 도시 집합에 추가한다.
                selected_citys.append(u)
        
    # visited를 완성한 후 city와 길이를 비교했을 때 같다면
    if len(visited) == len(city):
        # 둘 다 연결리스트가 성립되므로 True(1)를 리턴
        return 1
    # 아니라면 False(0)를 리턴한다
    else: 
        return 0

# 정답을 받을 배열
answer = []

# powerset은 yield를 사용해 선택한 도시의 집합(sel)과 선택하지 않은 도시의 집합(unsel)를 반환한다.
for sel, unsel in powerset(list(city.keys())):
    
    # 둘 다 참이라면. 즉 한 집합이 전체집합이고 다른 집합이 공집합인 경우가 아니라면
    if sel and unsel:
       
        # 우선 각 집합에서의 사람의 수를 0으로 초기화한다.
        sel_people, unsel_people = 0, 0
        
        # 선택된 도시들의 연결 상태와 선택되지 않은 도시들의 연결 상태를 확인한다. 둘 다 참이어야 조건을 만족할 수 있다. 
        if bfs(sel[0], unsel) and bfs(unsel[0], sel):

            # 조건을 만족했다면 각 도시 집합들의 인구 수를 구한다.
            for i in sel:
                sel_people += population[i]
            for i in unsel:
                unsel_people += population[i]
            
            # 정답 배열에 두 집합의 인구 수 차를 절댓값으로 받는다. 음수로 인한 오차 방지.
            answer.append(abs(sel_people-unsel_people))

# 인구 수의 차이가 최소인 것을 찾아야 하므로 min(answer)를 출력
if answer:
    print(min(answer))

# 두 선거구로 나눌 수 없는 경우 -1을 출력
else:
    print(-1)


''' 주석 없는 코드
import sys
read = sys.stdin.readline

N = int(read())
population = [0] + list(map(int, read().split()))

city = dict()
for i in range(1, N+1):
    city[i] = list(map(int, read().split()))[1:]

def powerset(set):
    masks = [1 << i for i in range(len(set))]
    for i in range(1 << len(set)):
        yield [element for mask, element in zip(masks, set) if mask & i], [element for mask, element in zip(masks, set) if mask & (-i-1)]

def bfs(start, unselected_citys):

    visited = {i: 1 for i in unselected_citys}    
    visited[start] = 1   
    
    selected_citys = [start]

    for v in selected_citys:
        for u in city[v]:
            if u not in visited:
                visited[u] = 1
                selected_citys.append(u)
        
    if len(visited) == len(city):
        return 1
    else: 
        return 0

answer = []

for sel, unsel in powerset(list(city.keys())):
    if sel and unsel:
        sel_people, unsel_people = 0, 0

        if bfs(sel[0], unsel) and bfs(unsel[0], sel):
            for i in sel:
                sel_people += population[i]
            for i in unsel:
                unsel_people += population[i]
            answer.append(abs(sel_people-unsel_people))

if answer:
    print(min(answer))
else:
    print(-1)
'''