class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")


def earliest_ancestor(ancestors, starting_vertex):
    # Build the graph
    g = Graph()

    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])

        # Build edges in reverse
        g.add_edge(pair[1], pair[0])

    # Do a BFS (storing the path)
    q = Queue()
    q.enqueue([starting_vertex])
    # Create a Set to store visited vertices
    max_path_len = 1
    earliest_ancestor = -1

    # # While the queue is not empty...
    while q.size() > 0:
        # Dequeue the first PATH
        path = q.dequeue()

        # Grab the first vertex from the PATH
        v = path[-1]

        # If the path is longer or equal and the value is smaller, or if the path is longer

        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)

        for next_node in g.vertices[v]:
            new_path = list(path)
            new_path.append(next_node)
            q.enqueue(new_path)

    return earliest_ancestor
