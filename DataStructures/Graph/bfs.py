def bfs(grafo,source):
    visited = []
    queue = [source]
    while len(queue) > 0:
        elem = queue.pop(0)
        if elem not in visited:
            visited.append(elem)
            for nodo in grafo[elem]:
                if nodo not in visited:
                    queue.append(nodo)
                
    return visited
