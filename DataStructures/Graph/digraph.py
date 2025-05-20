from DataStructures.Graph import edge
from DataStructures.Graph import vertex
from DataStructures.Map import map_linear_probing as mp

def new_graph(order):
    graph = {'vertices':mp.new_map(order),
             'num_edges':0}
    return graph

def insert_vertex(graph,key,info):
    if key != None and graph != None:
        nodo = vertex.new_vertex(key,info)
        graph['vertices'] = mp.put(graph['vertices'],key,nodo)
    return graph

def update_vertex_info(graph,key,info): #da.rincon
    vertices = graph["vertices"]
    vertice = mp.get(vertices,key)
    vertex.set_value(vertice,info)
    return graph

def remove_vertex(graph,key):
    if graph != None and key != None:
        info_eliminado = mp.get(graph['vertices'],key) 
        adj_elim = mp.key_set(info_eliminado['adjacents'])
        for adj in adj_elim:
            mp.remove(mp.get(graph['vertices'],adj)['adjacents'],key)
            graph['edges'] -= 1
        graph['vertices'] = mp.remove(graph['vertices'],key)
    return graph

def add_edge(graph, key_u, key_v, weight=1.0):#ncastano
    
    if not mp.contains(graph['vertices'], key_u):
        raise Exception("Vertex not found")
        
    if not mp.contains(graph['vertices'], key_v):
        raise Exception("Vertex not found")

    if key_u in graph['vertices'] and key_v in graph['vertices']:
        u = mp.get(graph['vertices'], key_u)
        v = mp.get(graph['vertices'], key_v)
        e = edge.new_edge(u, v, weight)
        u.add_edge(e)
        v.add_edge(e)
        graph['edges'] += 1
    return graph

def order(graph):
    vertices = mp.size(graph['vertices'])
    if vertices == 0:
        raise Exception("Graph is empty")
    if vertices > 0:
        return int(vertices)
        
    return vertices.s

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
