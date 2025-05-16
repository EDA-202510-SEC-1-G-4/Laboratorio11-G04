from DataStructures.Graph import edge
from DataStructures.Graph import vertex
from DataStructures.Map import map_linear_probing as mp

def new_graph(order):
    graph = {'vertices':mp.new_map(order),
             'num_edges':0}
    return graph

def insert_vertex(): #jecheverry
    return

def update_vertex_info(graph,key,info): #da.rincon

    map = graph["vertices"]
    vertice = mp.get(map,key)
    vertex.set_value(vertice,info)
    
    return graph

def remove_vertex(): #jecheverry
    return

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
