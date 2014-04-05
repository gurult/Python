from topological_sort import Topological_sort

grafas = Topological_sort()
grafas.read_graph_edges_from_file("input.txt")
grafas.make_vertex_list()
print(grafas.graph_edges)
# print("------------")
grafas.find_suns_of_vertex()
grafas.topological_sorting()
grafas.print_info_of_votexes()