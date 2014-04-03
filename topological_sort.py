
class Vertex:

    def __init__(self, vertex):

        self.vertex = vertex  # name of vertex
        self.suns = []        # childs of vertex
        self.father = -1      # father of vertex then sorted, can be only one
        self.mark = -1        # not visited -1, temporary mark 0, visited 1

    def print_info(self):

        print()
        # print("virsune " + str(self.vertex))
        print("virsune %s" % self.vertex)
        print("sunus " + str(self.suns))
        print("tevas yra : " + str(self.father))
        print("žyme: " + str(self.mark))
        print()