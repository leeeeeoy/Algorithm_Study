def virus_DFS(network, start):
    visited, need_visited = list(), list()

    need_visited.append(start)

    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(network[node])

    return len(visited) - 1


node = int(input())
edge = int(input())

network = dict()

for i in range(edge):
    node1, node2 = map(int, input().split())

    if node1 not in network:
        network[node1] = [node2]
    elif node2 not in network[node1]:
        network[node1].append(node2)

    if node2 not in network:
        network[node2] = [node1]
    elif node1 not in network[node2]:
        network[node2].append(node1)

print(virus_DFS(network, 1))
