# """
# Simple graph implementation
# """
# from util import Stack, Queue  # These may come in handy


# class Graph:

#     """Represent a graph as a dictionary of vertices mapping labels to edges."""

#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex_id):
#         """
#         Add a vertex to the graph.
#         """
#         self.vertices[vertex_id] = set()

#     def add_edge(self, v1, v2):
#         """
#         Add a directed edge to the graph.
#         """
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise IndexError('that vertex is non-existent')

#     def get_neighbors(self, vertex_id):
#         """
#         Get all neighbors (edges) of a vertex.
#         """
#         return self.vertices[vertex_id]

#     def bft(self, starting_vertex):
#         """
#         Print each vertex in breadth-first order
#         beginning from starting_vertex.
#         """

#         # create queue for where I need to visit still   
#         to_visit = Queue()
#         to_visit.enqueue(starting_vertex)
#         # create set for where I have already visited
#         visted_ver = set()


#         while to_visit.size() > 0:
#             # remove the first vertex on the queue
#             current_vertex = to_visit.dequeue()

            
#             if current_vertex not in visted_ver:


#                 print(current_vertex)


#                 # add this vertex to the visited ones
#                 visted_ver.add(current_vertex)


#                 # unvisted to queue
#                 for neighbor in self.get_neighbors(current_vertex):
#                     if neighbor not in visted_ver:
#                         to_visit.enqueue(neighbor)

#     def dft(self, starting_vertex):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
#         """
#        # Stack instead of queue for DF
#         to_visit = Stack()
#         to_visit.push(starting_vertex)
#         visited_ver = set()


#         # go as long as there are still rooms to visit
#         while to_visit.size() > 0:
#             current_vertex = to_visit.pop()
            
            
            
#             # if it has not been visited
#             if current_vertex not in visited_ver:
#                 print(current_vertex)
                

#                 # make sure we add the current vertex to the set of visited ones
#                 visited_ver.add(current_vertex)


#                 # add the neighbors of current node to the nodes to visit list if they have not been visited yet
#                 for neighbor in self.get_neighbors(current_vertex):
#                     if neighbor not in visited_ver:
#                         to_visit.push(neighbor)

#     def dft_recursive(self, starting_vertex, visited_vertices=None):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
#         This should be done using recursion.
#         """
#         if visited_vertices is None:
#             visited_vertices = set()


#         visited_vertices.add(starting_vertex)
#         print(starting_vertex)
#         neighbors = self.get_neighbors(starting_vertex)



#         # we check for neighbors in the current node
#         while len(neighbors) > 0:
#             for neighbor in neighbors:
#                 # if the neighbor is not in the visited vertices
#                 if neighbor not in visited_vertices:
                    
#                     # RECURSION TIME!!! passing in the neighbor of the current node and all the vertices we already visited
#                     self.dft_recursive(neighbor, visited_vertices)
#                 else:
#                     return

#     def bfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing the shortest path from
#         starting_vertex to destination_vertex in
#         breath-first order.
#         """

#         # bf so queue
#         bft_path = Queue()
#         bft_path.enqueue([starting_vertex])
#         visited_vertices = set()



#         # while queue is not empty
#         while bft_path.size() > 0:
#             # dequeue the first Path and add it to the current path
#             curr_path = bft_path.dequeue()



#             # grab the last vertex in the path
#             curr_path_last_vertex = curr_path[-1]
            
            
#             # if the most recently added node hasnt been visited
#             if curr_path_last_vertex not in visited_vertices:
                
                
#                 # check if its the target
#                 if curr_path_last_vertex == destination_vertex:
#                     return curr_path
                
                
                
#                 # mark it as visited if it is not
#                 else:
#                     visited_vertices.add(curr_path_last_vertex)
#                     neighbors = self.get_neighbors(curr_path_last_vertex)
                
                
                
#                     for neighbor in neighbors:

#                         # duplicate the path <------
#                         curr_path_copy = curr_path[:]

#                         curr_path_copy.append(neighbor)
#                         bft_path.enqueue(curr_path_copy)

#     def dfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing a path from
#         starting_vertex to destination_vertex in
#         depth-first order.
#         """
#         # depth = stack
#         dfs_path = Stack()
#         dfs_path.push([starting_vertex])
#         visited_vertices = set()
        
        
        
        
        
#         # while path is not empty
#         while dfs_path.size() > 0:
#             curr_path = dfs_path.pop()
#             curr_path_last_vertex = curr_path[-1]
            
            
#             # if we havent been to the current node
#             if curr_path_last_vertex not in visited_vertices:
                
#                 # check if node is the destination
#                 if curr_path_last_vertex == destination_vertex:
                    
                    
#                     # return the entire path if it is
#                     return curr_path
                
                
#                 # mark as visited if it is not
#                 else:
                    
                    
#                     # get the neighbors / make new versions on the path
#                     visited_vertices.add(curr_path_last_vertex)
#                     neighbors = self.get_neighbors(curr_path_last_vertex)
                    
                    
                    
#                     for neighbor in neighbors:
#                         # duplicate the path
#                         curr_path_copy = curr_path[:]
#                         # add the neighbor
#                         curr_path_copy.append(neighbor)
#                         # add the new path
#                         dfs_path.push(curr_path_copy)

#     def dfs_recursive(self, starting_vertex, destination_vertex, dfs_path=Stack(), visited_ver=None):
#         """
#         Return a list containing a path from
#         starting_vertex to destination_vertex in
#         depth-first order.
#         This should be done using recursion.
#         """
#         visited_ver = set()
#         curr_path = dfs_path.pop()
        
        
#         if curr_path == None:
#             curr_path = [starting_vertex]


#         # check if the most recently added is not in visited 
#         if curr_path[-1] not in visited_ver:


#             # if not there add it to visited
#             visited_ver.add(curr_path[-1])
#             # get neighbors for the last item,
#             for neighbor in self.get_neighbors(curr_path[-1]):
                
                
#                 # if neighbor is the destination vertex, end this
#                 if neighbor == destination_vertex:
                    
                    
#                     # add the destination neighbor to path
#                     curr_path.append(neighbor)
#                     return curr_path
                
                
#                 # create a copy of the curr path to make a new path
#                 curr_path_copy = curr_path.copy()
#                 # add neighbor to new path
#                 curr_path_copy.append(neighbor)
#                 # push the new path to the master path
#                 dfs_path.push(curr_path_copy)
            
            
#             # RECURSION TIME!!!
#             return self.dfs_recursive(starting_vertex, destination_vertex, dfs_path, visited_ver)


# if __name__ == '__main__':
#     graph = Graph() 
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)
#     graph.add_vertex(4)
#     graph.add_vertex(5)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_edge(5, 3)
#     graph.add_edge(6, 3)
#     graph.add_edge(7, 1)
#     graph.add_edge(4, 7)
#     graph.add_edge(1, 2)
#     graph.add_edge(7, 6)
#     graph.add_edge(2, 4)
#     graph.add_edge(3, 5)
#     graph.add_edge(2, 3)
#     graph.add_edge(4, 6)

#     '''
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
#     print(graph.vertices)

#     '''
#     Valid BFT paths:
#         1, 2, 3, 4, 5, 6, 7
#         1, 2, 3, 4, 5, 7, 6
#         1, 2, 3, 4, 6, 7, 5
#         1, 2, 3, 4, 6, 5, 7
#         1, 2, 3, 4, 7, 6, 5
#         1, 2, 3, 4, 7, 5, 6
#         1, 2, 4, 3, 5, 6, 7
#         1, 2, 4, 3, 5, 7, 6
#         1, 2, 4, 3, 6, 7, 5
#         1, 2, 4, 3, 6, 5, 7
#         1, 2, 4, 3, 7, 6, 5
#         1, 2, 4, 3, 7, 5, 6
#     '''
#     graph.bft(1)

#     '''
#     Valid DFT paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
#     graph.dft(1)
#     graph.dft_recursive(1)

#     '''
#     Valid BFS path:
#         [1, 2, 4, 6]
#     '''
#     print(graph.bfs(1, 6))

#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
#     print(graph.dfs(1, 6))
#     print(graph.dfs_recursive(1, 6))



class Graph:
    def __init__(self):
        self.node = {}

    def add_node(self, value):
        if value not in self.node:
            self.node[value] = set()

    def add_edge(self, v1, v2):
        self.node[v1].add(v2)

    def get_neighbor(self, value):
        return self.node[value]

    def dfs(self, start, visited=None, path=None, result=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if result is None:
            result = []
        path = path + [start]
        if len(self.get_neighbor(start)) == 0 and len(visited) == 0:
            return -1
        elif len(self.get_neighbor(start)) == 0:
            result.append((start, len(path)))
        for parent in self.get_neighbor(start):
            visited.add(start)
            self.dfs(parent, visited, path, result)
        return result
