graph = {
    '5': ['3', '7'],
    '3': ['2', '4', '5'],
    '7': ['8', '5'],
    '2': [],
    '4': ['8', '3'],
    '8': ['4', '7']
}
visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node):
    visited.append(node)
    queue = [node]
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("-->> Depth-First Search <<--")
print("\n\tVisited: ", end=" ")
dfs(visited, graph, '4')

visited = []
print("\n\n--->> Breadth-First Search <<---")
print("\n\tVisited: ", end=" ")
bfs(visited, graph, '4')
