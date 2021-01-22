# 네트워크에서 연결된 컴퓨터들을 찾기 위한 DFS 알고리즘
# DFS는 stack처럼, BFS는 queue처럼 사용한다.
def virus_DFS(network, start):
    # visited : 이미 방문하여 더이상 방문할 필요 없는 노드 리스트
    # need_visited : 아직 방문하지 않은 노드 리스트
    visited, need_visited = list(), list()

    # 시작 지점부터 방문해야 하기 때문에 가장 처음에 start를 넣는다.
    need_visited.append(start)

    # 방문해야 할 노드가 남아있다면
    while need_visited:

        # stack처럼 사용하기 때문에 가장 마지막에 들어온 노드를 꺼냄
        node = need_visited.pop()

        # 해당 노드가 아직 방문하지 않는 노드라면
        if node not in visited:
            # 방문한 노드 리스트에 추가
            visited.append(node)

            # 방금 방문한 노드에 연결된 노드 리스트를 아직 방문하지 않는 노드 리스트에 전부 추가
            need_visited.extend(network[node])

    # 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 '수'를 출력해야 함
    # visited는 1번 컴퓨터와 연결된 컴퓨터(감염된 컴퓨터)들의 리스트이고
    # 이것의 전체 길이에서 1번 컴퓨터는 빼야 한다.
    return len(visited) - 1


# 컴퓨터(노드)의 수와 연결된 쌍(간선)의 수
node = int(input())
edge = int(input())

# 그래프를 그리기 위해 네트워크는 딕셔너리로 설정
network = dict()

# 간선의 수만큼 돌면서
for i in range(edge):
    
    # 각 노드를 받은 후
    node1, node2 = map(int, input().split())

    # 노드1이 네트워크에 없다면
    if node1 not in network:
        # node1을 key값으로 설정 후 node2를 리스트 형태로 node1의 value로 넣는다.
        network[node1] = [node2]
        
    # node2가 node1의 value가 아니라면
    elif node2 not in network[node1]:
        
        # node2를 node1의 value로 추가해준다.
        network[node1].append(node2)

    # 연결된 한 쌍이기 때문에 양방향 그래프이다. node1->node2를 해주었으니 반대로도 해주자
    if node2 not in network:
        network[node2] = [node1]
    elif node1 not in network[node2]:
        network[node2].append(node1)

# 완성된 그래프와 시작 지점인 1번 컴퓨터를 DFS에 인자로 넣고 출력
print(virus_DFS(network, 1))
