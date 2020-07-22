# class Node(object):
#     def __init__(self, val=None):
#         self.value = val

class Graph(object):
    def __init__(self):
        self.num_vertices = 0
        self.vertices = []
        self.connections = {}

    def add_vertex(self, val):
        if val not in self.vertices:
            self.vertices.append(val)
            self.connections[val] = set()
            self.num_vertices += 1
    
    def add_edge(self, val1, val2):
        if val1 in self.vertices and val2 in self.vertices:
            self.connections[val1].add(val2)

    def show_connections(self):
        for key in self.connections:
            print(key, '->')
            for val in self.connections[key]:
                print(val)


a = Graph()
a.add_vertex(1)
a.add_vertex(2)
a.add_vertex(3)
a.add_vertex(4)
a.show_connections()
a.add_edge(1, 2)
a.add_edge(2, 3)
a.add_edge(3, 4)
a.add_edge(4, 1)
a.show_connections()



