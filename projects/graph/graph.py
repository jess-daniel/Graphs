"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex Does Not Exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()

        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                print(v)
                visited.add(v)
                for next_v in self.get_neighbors(v):
                    q.enqueue(next_v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()

        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                print(v)
                visited.add(v)
                for next_v in self.get_neighbors(v):
                    s.push(next_v)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # we need a base case
        # we need to call dft_recursive
        # we need to move towards the base case
        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        print(starting_vertex)

        for v in self.vertices[starting_vertex]:
            if v not in visited:
                self.dft_recursive(v, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty Queue and enqueue path to starting vertex id
        q = Queue()

        q.enqueue([starting_vertex])
        # create a set to store the visited vertices
        visited = set()
        # while the is not empty
        while q.size() > 0:
            # dequeue the first path
            path = q.dequeue()
            # grab the last vertex from the path
            v = path[-1]
            # check whether vertex has not been visited
            # check to see if it's the target
            if v not in visited:
                # if it is, return specific path
                if v == destination_vertex:
                    return path
                # if it's not, mark as visited
                visited.add(v)
                # then add a path to neighbors to back of queue
                for next_vertext in self.get_neighbors(v):
                    # make a copy of the path
                    path_copy = list(path)
                    # append neighbor to the back of path
                    path_copy.append(next_vertext)
                    # enqueue out new path
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()

        s.push([starting_vertex])
        # create a set to store the visited vertices
        visited = set()
        # while the is not empty
        while s.size() > 0:
            # dequeue the first path
            path = s.pop()
            # grab the last vertex from the path
            v = path[-1]
            # check whether vertex has not been visited
            # check to see if it's the target
            if v not in visited:
                # if it is, return specific path
                if v == destination_vertex:
                    return path
                # if it's not, mark as visited
                visited.add(v)
                # then add a path to neighbors to back of queue
                for next_vertext in self.get_neighbors(v):
                    # make a copy of the path
                    path_copy = list(path)
                    # append neighbor to the back of path
                    path_copy.append(next_vertext)
                    # enqueue out new path
                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path += [starting_vertex]
        v = path[len(path)-1]
        if visited is None:
            visited = set()

        if v not in visited:
            if v is destination_vertex:
                if path[len(path) - 1] is destination_vertex:
                    return path
            else:
                visited.add(v)

                for next_v in self.get_neighbors(v):
                    path_copy = [item for item in path]
                    temp = self.dfs_recursive(
                        next_v, destination_vertex, path_copy, visited)
                    if temp is not None:
                        return temp


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
