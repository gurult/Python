# author Ruslan Bulko


import os


class Topological_sort:

    vertex_list = []
    is_graph_dag = True  # if value false graph can't be sorted

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

    # print information about all vertexes
    def topological_sorting(self):
        sorted_list = []
        for vertex in self.vertex_list:
            if vertex.mark == -1:
                self.visit(vertex, sorted_list)
        if not self.is_graph_dag:
            return None
        return sorted_list

    # function is supporting and checks graph is it dag or not and takes
    # two parameters vertex which was constructed from edges and
    # sorted_list which will be returned end vertexes will be sorted
    # if it possible
    def visit(self, vertex, sorted_list):
        if vertex.mark == 0:
            self.is_graph_dag = False
        if vertex.mark == -1:
            vertex.mark = 0
            if vertex.suns == 0:
                return sorted_list.insert(0, vertex.vertex)
            for next_vertex in self.vertex_list:
                for i in range(len(vertex.suns)):
                    if next_vertex.vertex == vertex.suns[i]:
                        next_vertex.father = vertex.vertex
                        self.visit(next_vertex, sorted_list)
            vertex.mark = 1
            return sorted_list.insert(0, vertex.vertex)

    def sort(self, file_name):
        self.read_graph_edges_from_file(file_name)
        self.make_vertex_list()
        print("the edges of the graph")
        print(self.graph_edges)
        # print("------------")
        sorted = []
        sorted = self.topological_sorting()
        if sorted is None:
            print("Grpah is not dag and can't be sorted")
        else:
            print(" topologicaly sorted : ")
            print(sorted)


class Vertex:

    def __init__(self, vertex):

        self.vertex = vertex  # name of vertex
        self.suns = []        # childs of vertex
        self.father = -1      # father of vertex then sorted, can be only one
        self.mark = -1        # not visited -1, temporary mark 0, visited 1

    def print_info(self):

        print()
        print("Vertex : %s" % self.vertex)
        print("Suns : " + str(self.suns))
        print("Father is : " + str(self.father))
        print("Mark : " + str(self.mark))
        print()