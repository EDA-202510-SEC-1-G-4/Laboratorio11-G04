from DataStructures.List import array_list as al
from DataStructures.Stack import stack as s
from DataStructures.Graph import digraph as G

def dfs(grafo,source):
    visited = al.new_list()
    stack = s.new_stack()
    s.push(stack,source)
    while s.size(stack) > 0:
        elem = s.pop(stack)
        if elem not in visited['elements']:
            al.add_last(visited,elem)
            for nodo in G.adjacents(grafo,source)['elements']:
                if nodo not in visited['elements']:
                    s.push(stack,nodo)
    return visited

