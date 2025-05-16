from DataStructures.Graph import digraph as D

graph = D.new_graph(1)
my_graph = D.insert_vertex(graph, "Madrid", {"nombre": "Madrid", "pais": "España"})
print(my_graph)
