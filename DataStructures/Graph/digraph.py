from DataStructures.Graph import edge
from DataStructures.Graph import vertex
from DataStructures.Map import map_linear_probing as mp

def new_graph(order):
    graph = {'vertices':mp.new_map(order),
             'edges':0}
    return graph

def insert_vertex(): #jecheverry
    return

def update_vertex_info():
    return

def remove_vertex(): #jecheverry
    return

def add_edge(graph, key_u, key_v, weight=1.0):#ncastano
    
    if not mp.contains(graph['vertices'], key_u):
        return KeyError("Vertex not found")
        
    if not mp.contains(graph['vertices'], key_v):
        return KeyError("Vertex not found")

    if key_u and key_v in graph['vertices']:
        u = mp.get(graph['vertices'], key_u)
        v = mp.get(graph['vertices'], key_v)
        e = edge.new_edge(u, v, weight)
        u.add_edge(e)
        v.add_edge(e)
        graph['edges'] += 1
    return graph

def order():
    return

def size():
    return

def vertices():
    return

def degree():
    return

def get_edge():
    return

def get_vertex_information():
    return

def contains_vertex(): #Jecheverry
    return

def adjacents(): #jecheverry
    return

def edges_vertex():
    return

def get_vertex(): #jecheverry
    return
