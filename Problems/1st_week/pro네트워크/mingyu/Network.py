def network_BFS(network, start):
    # 이미 방문한 노드들의 리스트, 방문하여 확인해야 할 노드들의 stack
    visited, need_visit = list(), list()

    # 시작 노드부터 확인하기 위해 need_visit에 start를 넣는다.
    need_visit.append(start)

    # 방문해야 할 노드가 더 없을 때까지
    while need_visit:
        # 방문해야 할 노드 리스트의 첫번째 값을 꺼내온다. (queue처럼 사용)
        node = need_visit.pop(0)

        # 해당 노드가 방문한 적 없는 노드라면
        if node not in visited:
            # 방문한 노드 리스트에 node를 집어넣고
            visited.append(node)

            # 해당 노드에 연결된 값들을 방문해야 할 노드 리스트에 추가한다.
            need_visit.extend(network[node])

    # 이후 중복을 제거하기 위해 배열을 정렬된 상태로 반환한다.
    return sorted(visited)


def solution(n, computers):
    # 네트워크의 그래프를 딕셔너리로 선언
    network = dict()

    # 그래프 그리기
    # 무방향(양방향)그래프인데, 어차피 2중 for문 안에서 양방향으로 돌아가기 때문에
    # 굳이 if/elif문을 두 번 써줄 필요는 없다.
    for node_l in range(n):
        for node_r in range(len(computers[node_l])):

            # computers[node_l][node_r]이 1(True)이어야만 두 노드(컴퓨터)가 연결된 것이다.
            if computers[node_l][node_r]:
                # 왼쪽 노드(node_l)이 네트워크에 없으면
                if node_l not in network:
                    # node_l을 키로 하고 node_r을 리스트 형태의 value로 넣는다.
                    network[node_l] = [node_r]

                # 키(node_l) 값이 이미 네트워크에 존재한다면
                elif node_l in network:
                    # 해당 키에 value값만 추가
                    network[node_l].append(node_r)

    # 중복을 제거하고 넣을 set 리스트. 어째서인지 set(array)가 되지 않아서 이렇게 만들었다.
    set = []

    # 네트워크가 가진 노드의 수만큼 돌면서
    for i in range(len(network)):

        # 중복 제거용 알고리즘
        # BFS 알고리즘을 돌아 나온 배열이 set에 아직 없다면
        if network_BFS(network, i) not in set:
            # 중복되지 않은 배열이므로 set에 추가한다.
            set.append(network_BFS(network, i))

    # set에는 각 노드들끼리 연결된 배열, 즉 서로 연결된 노드들끼리의 집합이 들어가 있다.
    # 해당 집합의 수가 네트워크의 개수이므로 이것을 출력
    print(len(set))
