from DataStructures.Graph import edge
from DataStructures.Graph import vertex
from DataStructures.Map import map_linear_probing as mp

def new_graph(order):
    graph = {'vertices':mp.new_map(order),
             'edges':0}
    return graph

def insert_vertex(graph,key,info):
    if key != None and graph != None:
        graph['vertices'] = mp.put(graph['vertices'],key,info)
    return graph

def update_vertex_info():
    return

def remove_vertex(graph,key):
    if graph != None and key != None:
        info_eliminado = mp.get(graph['vertices'],key) 
        adj_elim = mp.key_set(info_eliminado['adjacents'])
        for adj in adj_elim:
            info_adj = mp.get(graph['vertices'],adj)
            info_adj['adjacents'] = mp.remove(info_adj['adjacents'],key)
            graph['edges'] -= 1
        graph['vertices'] = mp.remove(graph['vertices'],key)
    return graph

def add_edge():
    return

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
