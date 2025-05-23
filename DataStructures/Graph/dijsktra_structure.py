from DataStructures.Map import map_linear_probing as mp
from DataStructures.Priority_queue import priority_queue as pq


def new_dijsktra_structure(source, g_order):
    """

    Crea una estructura de busqueda usada en el algoritmo **dijsktra**.

    Se crea una estructura de busqueda con los siguientes atributos:

    - **source**: Vertice de origen. Se inicializa en ``source``
    - **visited**: Mapa con los vertices visitados. Se inicializa en ``None``
    - **pq**: Cola indexada con los vertices visitados. Se inicializa en ``None``

    :returns: Estructura de busqueda
    :rtype: dijsktra_search
    """
    structure = {
        "source": source,
        "visited": mp.new_map(
            g_order, 0.5),
        "pq": pq.new_heap()}
    return structure

def dijkstra(my_graph, source):
    
    if not mp.contains(my_graph['vertices'], source):
        raise Exception("El vértice fuente no existe en el grafo")
    

    g_order = mp.size(my_graph['vertices'])
    search_struct = new_dijsktra_structure(source, g_order)
    
    dist_to = mp.new_map(g_order, 0.5)
    edge_to = mp.new_map(g_order, 0.5)
    for vertex in mp.key_set(my_graph['vertices']):
        mp.put(dist_to, vertex, float('inf'))
        mp.put(search_struct['visited'], vertex, False)
    
    mp.put(dist_to, source, 0)
    pq.insert(search_struct['pq'], source, 0)
    
    while not pq.is_empty(search_struct['pq']):
        current_vertex = pq.del_min(search_struct['pq'])
        
        if mp.get(search_struct['visited'], current_vertex):
            continue
        
        mp.put(search_struct['visited'], current_vertex, True)
        
        vertex = mp.get(my_graph['vertices'], current_vertex)
        adjacents = mp.key_set(vertex['adjacents'])
        
        for neighbor in adjacents:
            edge = mp.get(vertex['adjacents'], neighbor)
            new_dist = mp.get(dist_to, current_vertex) + edge['weight']
            
            if new_dist < mp.get(dist_to, neighbor):
                mp.put(dist_to, neighbor, new_dist)
                mp.put(edge_to, neighbor, current_vertex)
                pq.insert(search_struct['pq'], neighbor, new_dist)
    
    result = search_struct.copy()
    result.update({
        'dist_to': dist_to,
        'edge_to': edge_to
    })
    
    return result


def dist_to(key_v, aux_structure):
    if not mp.contains(aux_structure['dist_to'], key_v):
        raise Exception("Vértice no encontrado en dist_to")
    return mp.get(aux_structure['dist_to'], key_v)

def has_path_to(key_v, aux_structure):
    return mp.get(aux_structure['dist_to'], key_v) < float('inf')

def path_to(key_v, aux_structure):
    if not has_path_to(key_v, aux_structure):
        raise Exception("No existe camino al vértice")
    
    path = []
    current = key_v
    
    while current is not None and current != aux_structure['source']:
        path.append(current)
        current = mp.get(aux_structure['edge_to'], current)
    
    path.append(aux_structure['source'])
    path.reverse()
    
    return path