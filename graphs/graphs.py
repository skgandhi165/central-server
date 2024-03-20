# Source: https://experiencestack.co/graph-implementation-in-python-916fc3b6a8a

class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.neighbours = []


    def add_neighbour(self, neighbour):
        if neighbour not in self.neighbours:
            self.neighbours.append(neighbour)


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []


    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.id not in self.vertices:
            self.vertices[vertex.id] = vertex
            return True
        else:
            return False


    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add_neighbour(v2)
            self.vertices[v2].add_neighbour(v1)
            self.edges.append({v1, v2})
            return True
        else:
            return False


    def get_vertices(self):
        return self.vertices.keys()

    def get_edges(self):
        return self.edges


    def __iter__(self):
        return iter(self.vertices.values())


# Create a graph with 4 vertices and 5 edges
graph = Graph()
# for i in range(4):
#      graph.add_vertex(Vertex(i))
# graph.add_edge(0, 1)
# graph.add_edge(0, 2)
# graph.add_edge(1, 2)
# graph.add_edge(1, 3)
# graph.add_edge(2, 3)
# nref = open("nref2ndfloor.csv", "r")
#  for i in range 

location = ""

with open('nref2ndfloor.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        location = line.strip().replace('"', '')
        vertex = Vertex(location)
        graph.add_vertex(vertex)

# graph

# for vertex in graph:
#     print(vertex.id)

# print(graph.get_vertices())

''' ROOM-TO-ROOM CONNECTION: probably not going to be implemented 
# graph.add_edge('2-001 Classroom', '2-003 Classroom')
# graph.add_edge('2-003 Classroom', '2-016 Classroom')
# graph.add_edge('2-016 Classroom', '2-020 Classroom')
# graph.add_edge('2-020 Classroom', '2-022 Help Desk Office')
# graph.add_edge('2-022 Help Desk Office', '2-030 ENV Grad Teaching Lab')
# graph.add_edge('2-030 ENV Grad Teaching Lab', '2-026 Teaching Prep Room')
# graph.add_edge('2-026 Teaching Prep Room', "2-026A ENV Lab Storage")
# graph.add_edge('2-026 Teaching Prep Room', '2-010 ENV Undergrad Teaching Lab')
# graph.add_edge('2-020 Classroom', '2-026 Teaching Prep Room')
# graph.add_edge('2-010 ENV Undergrad Teaching Lab', '2-052 Petroleum Undergrad Teaching Lab')
# graph.add_edge('2-080 Classroom', '2-090 Classroom')
# graph.add_edge('2-043 Mine Design Computational Lab', '2-080 Classroom')
# graph.add_edge('2-052 Petroleum Undergrad Teaching Lab', '2-080 Classroom')
# graph.add_edge('2-090 Classroom', '2-038 Civil Club Student Activity Room')
# graph.add_edge('2-038 Civil Club Student Activity Room', '2-039 Civil Club Office')
# graph.add_edge('2-039 Civil Club Office', '2-042 Storage')
# graph.add_edge('2-042 Storage', '2-047 Mining Club Office')
# graph.add_edge('2-047 Mining Club Office', '2-048 Petroleum Club Office')
'''

# ROOM TO HALLWAY CONNECTIONS
graph.add_edge('2-020ZZ Hallway with Sensor', '2-016 Classroom')
graph.add_edge('2-020ZZ Hallway with Sensor', '2-020 Classroom')
graph.add_edge('2-020ZZ Hallway with Sensor', '2-022 Help Desk Office')
graph.add_edge('2-020ZZ Hallway with Sensor', '2-030 ENV Grad Teaching Lab')
graph.add_edge('2-020ZZ Hallway with Sensor', '2-026 Teaching Prep Room')
graph.add_edge('2-020ZZ Hallway with Sensor', '2-010 ENV Undergrad Teaching Lab')
graph.add_edge('2-020ZZ Hallway with Sensor', 'STR-3 Stair 3')

graph.add_edge('2-001ZZ Hallway with Sensor', '2-001 Classroom')
graph.add_edge('2-001ZZ Hallway with Sensor', '2-003 Classroom')
graph.add_edge('2-001ZZ Hallway with Sensor', 'NREF Pedway')

graph.add_edge('2-118ZZ Hallway with Sensor', '2-118 Caterpillar Mining Engineering Design And Project Lab')
graph.add_edge('2-118ZZ Hallway with Sensor', '2-117 Computer Lab')
graph.add_edge('2-118ZZ Hallway with Sensor', '2-120 Printer/Server')
graph.add_edge('2-118ZZ Hallway with Sensor', '2-122 Classroom')
graph.add_edge('2-118ZZ Hallway with Sensor', '2-125 Computer Lab')
graph.add_edge('2-118ZZ Hallway with Sensor', '2-127 Classroom')
graph.add_edge('2-118ZZ Hallway with Sensor', 'STR-5 Stair 5')
graph.add_edge('2-118ZZ Hallway with Sensor', 'STR-1 Stair 1')
graph.add_edge('2-118ZZ Hallway with Sensor', 'ELV-179 Elevator')

graph.add_edge('2-043ZZ Hallway with Sensor', '2-090 Classroom')
graph.add_edge('2-043ZZ Hallway with Sensor', '2-038 Civil Club Student Activity Room')

graph.add_edge('2-042ZZ Hallway', '2-039 Civil Club Office')
graph.add_edge('2-042ZZ Hallway', '2-042 Storage')
graph.add_edge('2-042ZZ Hallway', '2-047 Mining Club Office')

graph.add_edge('2-080ZZ Hallway with Sensor', '2-052 Petroleum Undergrad Teaching Lab')
graph.add_edge('2-080ZZ Hallway with Sensor', '2-080 Classroom')
graph.add_edge('2-080ZZ Hallway with Sensor', '2-043 Mine Design Computational Lab')

graph.add_edge('2-004ZZ Hallway', '2-048 Petroleum Club Office')
graph.add_edge('2-004ZZ Hallway', '2-050 Office')
graph.add_edge('2-004ZZ Hallway', '2-051 Office')
graph.add_edge('2-004ZZ Hallway', '2-052 Petroleum Undergrad Teaching Lab')

# HALLWAY TO HALLWAY CONNECTION
graph.add_edge('2-001ZZ Hallway with Sensor', '2-002ZZ Hallway')
graph.add_edge('2-001ZZ Hallway with Sensor', '2-005ZZ Hallway')

graph.add_edge('2-002ZZ Hallway', '2-118ZZ Hallway with Sensor')
graph.add_edge('2-002ZZ Hallway', '2-011ZZ Hallway')

graph.add_edge('2-011ZZ Hallway', '2-005ZZ Hallway')
graph.add_edge('2-011ZZ Hallway', '2-060ZZ Hallway')
graph.add_edge('2-011ZZ Hallway', 'STR-6 Stair 6')

graph.add_edge('2-060ZZ Hallway', '2-118ZZ Hallway with Sensor')
graph.add_edge('2-060ZZ Hallway', '2-080ZZ Hallway with Sensor')
graph.add_edge('2-060ZZ Hallway', 'ELV-18X Elevators')
graph.add_edge('2-060ZZ Hallway', '2-043ZZ Hallway with Sensor')

graph.add_edge('2-020ZZ Hallway with Sensor', '2-001ZZ Hallway with Sensor')
graph.add_edge('2-020ZZ Hallway with Sensor', '2-005ZZ Hallway')
graph.add_edge('2-020ZZ Hallway with Sensor', 'STR-3 Stair 3')
graph.add_edge('2-005ZZ Hallway', 'STR-2 Stair 2')

graph.add_edge('2-042ZZ Hallway', '2-043ZZ Hallway with Sensor')
graph.add_edge('2-042ZZ Hallway', '2-080ZZ Hallway with Sensor')
graph.add_edge('2-042ZZ Hallway', '2-004ZZ Hallway')

graph.add_edge('2-004ZZ Hallway', '2-080ZZ Hallway with Sensor')
graph.add_edge('2-004ZZ Hallway', 'STR-4 Stair 4')


# graph.add_edge(, )
# graph.add_edge(, )
# graph.add_edge(, )
# graph.add_edge(, )
# graph.add_edge(, )
# graph.add_edge(, )



# for vertex in graph:
#     print(vertex.id)
#     print(vertex.neighbours)
for edges in graph.get_edges():
    print(edges)



