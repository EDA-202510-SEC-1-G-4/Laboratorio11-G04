from DataStructures.Graph import digraph as G
from DataStructures.Graph import dfs as DFS
# Crear un grafo vacío
my_graph = G.new_graph(10)

# Insertar vértices
my_graph = G.insert_vertex(my_graph, "Bogota", {})
my_graph = G.insert_vertex(my_graph, "Medellin", {})
my_graph = G.insert_vertex(my_graph, "Cali", {})
my_graph = G.insert_vertex(my_graph, "Barranquilla", {})
print(G.contains_vertex(my_graph, "Bogota"))  # debe ser True


# Agregar arcos (dirigidos)
print(G.contains_vertex(my_graph, "Bogota"))      # True
print(G.contains_vertex(my_graph, "Medellin"))    # True

my_graph = G.add_edge(my_graph, "Bogota", "Medellin", 1)
my_graph = G.add_edge(my_graph, "Medellin", "Cali", 1)
my_graph = G.add_edge(my_graph, "Cali", "Barranquilla", 1)

# Ejecutar DFS desde "Bogota"
dfs_result = DFS.dfs(my_graph, "Bogota")

# Mostrar los resultados del recorrido
print("Preorden:", dfs_result["pre"]["elements"])
print("Postorden:", dfs_result["post"]["elements"])
print("Reverse postorden (pila):", dfs_result["reversepost"]["elements"])
