import queue

graph = {'1': ['2', '3', '4'],
         '2': ['1', '3', '5'],
         '3': ['1', '2', '6', '7'],
         '4': ['1', '8'],
         '5': ['2', '6'],
         '6': ['3', '5'],
         '7': ['3'],
         '8': ['4']}

q = queue.Queue()


def bfs(graph, start, visited = []):
    q.put(start)
    while not q.empty():
        new_node = q.get()
        if new_node not in visited:
            visited.append(new_node)
            for i in graph[new_node]:
                q.put(i)
    return visited




print(bfs(graph,'3'))

