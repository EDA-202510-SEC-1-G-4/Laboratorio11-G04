from DataStructures.Graph import digraph as G

graph = G.new_graph(1)
my_graph = G.insert_vertex(graph, "Madrid", {"nombre": "Madrid", "pais": "España"})
my_graph = G.update_vertex_info(my_graph, "Madrid", {"nombre": "Madrid", "pais": "Colombia"})
print(my_graph)
