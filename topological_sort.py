# author Ruslan Bulko


import os


class Topological_sort:

    vertex_list = []

    def __init__(self):
        pass

    def read_graph_edges_from_file(self, file_name):

        if os.path.isfile(file_name):
            with open(file_name) as f:
                self.graph_edges = []
                for line in f:  # read rest of lines
                    self.graph_edges.append([int(x) for x in line.split(" ")])
            f.close()

    def make_vertex_list(self):
        templist = set()
        for element in self.graph_edges:
            for wortex in element:
                if wortex in templist:
                    pass
                else:
                    self.vertex_list.append(Vertex(wortex))
                    templist.add(wortex)
        self.vertex_list.sort(key=lambda x: x.vertex)

   # prints all information about vertexes
    def print_info_of_votexes(self):
        for i in range(0, len(self.vertex_list)):
            self.vertex_list[i].print_info()

    # find all suns of vertex
    def find_suns_of_vertex(self):
        for i in range(0, len(self.vertex_list)):
            for vertex in self.graph_edges:
                if len(vertex) == 1:
                    break
                elif self.vertex_list[i].vertex == vertex[0]:
                    self.vertex_list[i].suns.append(vertex[1])
                    self.vertex_list[i].suns.sort()


class Vertex:

    def __init__(self, vertex):

        self.vertex = vertex  # name of vertex
        self.suns = []        # childs of vertex
        self.father = -1      # father of vertex then sorted, can be only one
        self.mark = -1        # not visited -1, temporary mark 0, visited 1

    def print_info(self):

        print()
        # print("virsune " + str(self.vertex))
        print("Vertex : %s" % self.vertex)
        print("Suns : " + str(self.suns))
        print("Father is : " + str(self.father))
        print("Mark : " + str(self.mark))
        print()