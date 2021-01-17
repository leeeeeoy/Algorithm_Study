<<<<<<< HEAD
# 깊이 우선 탐색. stack으로 구현한다.
def DFS(graph, start_node):
    # 이미 방문한 노드들의 리스트, 방문하여 확인해야 할 노드들의 stack
    visited, need_visit = list(), list()

    # 시작 노드부터 확인하기 위해 need_visit에 start_node를 넣는다.
    need_visit.append(start_node)

    # 방문해야 할 노드가 더 없을 때까지
    while need_visit:
        # 방문해야 할 노드 리스트의 마지막 값을 꺼내온다. (stack처럼 사용)
        node = need_visit.pop()

        # 해당 노드가 방문한 적 없는 노드라면
        if node not in visited:
            # 방문한 노드 리스트에 node를 집어넣고
            visited.append(node)

            # 해당 노드에 연결된 값들을 방문해야 할 노드 리스트에 추가한다.
            # 이때 연결된 값들을 넣을 때, 제한사항으로 연결된 값들이 많으면 작은 값부터 사용한다고 한다.
            # 해당 graph는 stack으로 사용되어야 하기 때문에 가장 작은 값이 뒤에 오도록 내림차순 정렬하여 추가한다.
            need_visit.extend(sorted(graph[node], reverse=True))

    return " ".join(str(i) for i in visited)


# 너비 우선 탐색. queue로 구현한다.
def BFS(graph, start_node):
    # 이미 방문한 노드들의 리스트, 방문하여 확인해야 할 노드들의 stack
    visited, need_visit = list(), list()

    # 시작 노드부터 확인하기 위해 need_visit에 start_node를 넣는다.
    need_visit.append(start_node)

    # 방문해야 할 노드가 더 없을 때까지
    while need_visit:
        # 방문해야 할 노드 리스트의 첫번째 값을 꺼내온다. (queue처럼 사용)
        node = need_visit.pop(0)

        # 해당 노드가 방문한 적 없는 노드라면
        if node not in visited:
            # 방문한 노드 리스트에 node를 집어넣고
            visited.append(node)

            # 해당 노드에 연결된 값들을 방문해야 할 노드 리스트에 추가한다.
            # 이때 연결된 값들을 넣을 때, 제한사항으로 연결된 값들이 많으면 작은 값부터 사용한다고 한다.
            # 해당 graph는 queue로 사용되어야 하기 때문에 가장 작은 값은 가장 앞에 있어야 하므로 오름차순으로 정렬하여 추가한다.
            need_visit.extend(sorted(graph[node]))

    return " ".join(str(i) for i in visited)


def DFS_and_BFS():
    # 노드, 간선, 시작노드 값을 int형으로 받아온다.
    node, edge, start_node = map(int, input().split())

    # 그래프를 딕셔너리로 설정.
    graph = dict()

    # 간선의 수만큼 돈다. 입력의 개수 = 간선의 개수이다.
    for i in range(edge):

        # 양 노드를 int형으로 받아온다.
        node_left, node_right = map(int, input().split())

        # 주어진 그래프는 양방향 간선이다. 때문에 left -> right 방향과 right -> left 방향 모두를 처리해야 한다.
        # left -> right 부분부터 시작한다.
        if node_left not in graph:

            # key값(node_left)이 아직 graph 딕셔너리에 없는 경우 해당 key와 value(node_right)를 추가해준다.
            # 이때 value를 list 형식으로 추가한다.
            graph[node_left] = [node_right]

        # key는 존재하는데, value값이 key값에 포함되어 있지 않다면
        elif node_right not in graph[node_left]:

            # value는 현재 list 형식이다. 때문에 여기에는 append가 가능함
            graph[node_left].append(node_right)

        # 양방향 간선이기 떄문에 반대 방향으로도 처리한다.
        if node_right not in graph:
            graph[node_right] = [node_left]
        elif node_left not in graph[node_right]:
            graph[node_right].append(node_left)

    print(DFS(graph, start_node))
    print(BFS(graph, start_node))


print(DFS_and_BFS())
=======
# 깊이 우선 탐색. stack으로 구현한다.
def DFS(graph, start_node):
    # 이미 방문한 노드들의 리스트, 방문하여 확인해야 할 노드들의 stack
    visited, need_visit = list(), list()

    # 시작 노드부터 확인하기 위해 need_visit에 start_node를 넣는다.
    need_visit.append(start_node)

    # 방문해야 할 노드가 더 없을 때까지
    while need_visit:
        # 방문해야 할 노드 리스트의 마지막 값을 꺼내온다. (stack처럼 사용)
        node = need_visit.pop()

        # 해당 노드가 방문한 적 없는 노드라면
        if node not in visited:
            # 방문한 노드 리스트에 node를 집어넣고
            visited.append(node)

            # 해당 노드에 연결된 값들을 방문해야 할 노드 리스트에 추가한다.
            # 이때 연결된 값들을 넣을 때, 제한사항으로 연결된 값들이 많으면 작은 값부터 사용한다고 한다.
            # 해당 graph는 stack으로 사용되어야 하기 때문에 가장 작은 값이 뒤에 오도록 내림차순 정렬하여 추가한다.
            need_visit.extend(sorted(graph[node], reverse=True))

    return " ".join(str(i) for i in visited)


# 너비 우선 탐색. queue로 구현한다.
def BFS(graph, start_node):
    # 이미 방문한 노드들의 리스트, 방문하여 확인해야 할 노드들의 stack
    visited, need_visit = list(), list()

    # 시작 노드부터 확인하기 위해 need_visit에 start_node를 넣는다.
    need_visit.append(start_node)

    # 방문해야 할 노드가 더 없을 때까지
    while need_visit:
        # 방문해야 할 노드 리스트의 첫번째 값을 꺼내온다. (queue처럼 사용)
        node = need_visit.pop(0)

        # 해당 노드가 방문한 적 없는 노드라면
        if node not in visited:
            # 방문한 노드 리스트에 node를 집어넣고
            visited.append(node)

            # 해당 노드에 연결된 값들을 방문해야 할 노드 리스트에 추가한다.
            # 이때 연결된 값들을 넣을 때, 제한사항으로 연결된 값들이 많으면 작은 값부터 사용한다고 한다.
            # 해당 graph는 queue로 사용되어야 하기 때문에 가장 작은 값은 가장 앞에 있어야 하므로 오름차순으로 정렬하여 추가한다.
            need_visit.extend(sorted(graph[node]))

    return " ".join(str(i) for i in visited)


def DFS_and_BFS():
    # 노드, 간선, 시작노드 값을 int형으로 받아온다.
    node, edge, start_node = map(int, input().split())

    # 그래프를 딕셔너리로 설정.
    graph = dict()

    # 간선의 수만큼 돈다. 입력의 개수 = 간선의 개수이다.
    for i in range(edge):

        # 양 노드를 int형으로 받아온다.
        node_left, node_right = map(int, input().split())

        # 주어진 그래프는 양방향 간선이다. 때문에 left -> right 방향과 right -> left 방향 모두를 처리해야 한다.
        # left -> right 부분부터 시작한다.
        if node_left not in graph:

            # key값(node_left)이 아직 graph 딕셔너리에 없는 경우 해당 key와 value(node_right)를 추가해준다.
            # 이때 value를 list 형식으로 추가한다.
            graph[node_left] = [node_right]

        # key는 존재하는데, value값이 key값에 포함되어 있지 않다면
        elif node_right not in graph[node_left]:

            # value는 현재 list 형식이다. 때문에 여기에는 append가 가능함
            graph[node_left].append(node_right)

        # 양방향 간선이기 떄문에 반대 방향으로도 처리한다.
        if node_right not in graph:
            graph[node_right] = [node_left]
        elif node_left not in graph[node_right]:
            graph[node_right].append(node_left)

    print(DFS(graph, start_node))
    print(BFS(graph, start_node))


print(DFS_and_BFS())
>>>>>>> 388414e010420b3155986bca28c1b4ea0d95f317
