from DataStructures.List import array_list as al
from DataStructures.Queue import queue as q
from DataStructures.Graph import digraph as G

def bfs(grafo,source):
    visited = al.new_list()
    queue = q.new_queue()
    q.enqueue(queue,source)
    while q.size(queue) > 0:
        elem = q.dequeue(queue)
        if elem not in visited['elements']:
            al.add_last(visited,elem)
            for nodo in G.adjacents(grafo,elem)['elements']:
                if nodo not in visited['elements']:
                    q.enqueue(queue,nodo)
    return visited
