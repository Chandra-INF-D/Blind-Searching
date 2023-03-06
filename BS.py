class AdjacentNode:

    def __init__(self, vertex):

      self.vertex = vertex 
      self.next = None

#BidirectionalSearch implementation
class BidirectionalSearch:

    def __init__(self, vertices):

      #initialize vertices and
      #graph with vertices
      self.vertices = vertices
      self.graph = [None] * self.vertices

      #Initializing queue for forward
      #and backward search
      self.src_queue = list()
      self.dest_queue = list()

      #initializing source and
      #destination visited nodesas False
      self.src_visited = [False] * self.vertices
      self.dest_visited = [False] * self.vertices

      #initializing source and destination
      #parent nodes
      self.src_parent = [None] * self.vertices
      self.dest_parent = [None] * self.vertices

    #Function for adding undirected edge
    def add_edge(self, src, dest):

      #add edges to graph

      #add source to destination
      node = AdjacentNode(dest)
      node.next = self.graph[src]
      self.graph[src] = node

      #since graph is undirected add
      #destination to source
      node = AdjacentNode(src)
      node.next = self.graph[dest]
      self.graph[dest] = node

    #Function for breadht first search
    def bfs(self, direction = 'forward'):

      if direction == 'forward':

        #BFS in forward direction
        current = self.src_queue.pop(0)
        connected_node = self.graph[current]

        while connected_node:
          vertex = connected_node.vertex

          if not self.src_visited[vertex]:
            self.src_queue.append(vertex)
            self.src_visited[vertex] = True
            self.src_parent[vertex] = current

          connected_node = connected_node.next
      else:

       #BFS in backward direction
        current = self.dest_queue.pop(0)
        connected_node = self.graph[current]

        while connected_node:
          vertex = connected_node.vertex

          if not self.dest_visited[vertex]:
            self.dest_queue.append(vertex)
            self.dest_visited[vertex] = True
            self.dest_parent[vertex] = current

          connected_node = connected_node.next

    #connected for intersecting vertex
    def is_intersecting(self):

      #return intersecting node
      #if present else -1
      for i in range(self.vertices):
        if (self.src_visited[i] and
          self.dest_visited[i]):
          return i

      return -1
  
    #print the path from source to target
    def print_path(self, intersecting_node, src, dest):

      #print final path from
      #source to destination
      path = list()
      path.append(intersecting_node)
      i = intersecting_node

      while i != src:
        path.append(self.src_parent[i])
        i = self.src_parent[i]

      path = path[::-1]
      i = intersecting_node

      while i != dest:
        path.append(self.dest_parent[i])
        i = self.dest_parent[i]

      print("*****path******")
      path = list(map(str, path))

      print(' '.join(path))

    #Function fo bidirectional searching
    def bidirectional_search(self, src, dest):

        #add source to queue and mark
        #visited as true and add its 
        #parent as -1
        self.src_queue.append(src)
        self.src_visited[src] = True
        self.src_parent[src] = -1

        #Add destination to queue and
        #mark visited as true and add
        #its parent as -1 
        self.dest_queue.append(dest)
        self.dest_visited[dest] = True
        self.dest_parent[dest] = -1

        while self.src_queue and self.dest_queue:

          #BFS in forward direction from 
          #source vertex
          self.bfs(direction = 'forward')

        #BFS in reverse direction
        #from Destination vertex
        self.bfs(direction = 'backward')

        #check for intersecting vertex
        intersecting_node = self.is_intersecting()

        #If intersecting vertex exists
        #then path from source to
        #destination exists
        if intersecting_node != -1:
          print(f"path exists between {src} and {dest}")
          print(f"Intersection at : {intersecting_node}")
          self.print_path(intersecting_node, src, dest)

          exit(0)
        return -1
  
  #driver code
if __name__== '__main__':

#Number of vertices in graph
  n = 15

#source vertex
src = 0

#Destonation vertex
dest = 6

#create a graph 
graph = BidirectionalSearch(n)
graph.add_edge(0, 4)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 5)
graph.add_edge(4, 6)
graph.add_edge(5, 6)
graph.add_edge(6, 7)
graph.add_edge(7, 8)
graph.add_edge(8, 9)
graph.add_edge(8, 10)
graph.add_edge(9, 11)
graph.add_edge(9, 12)
graph.add_edge(10, 13)
graph.add_edge(10, 14)

out = graph.bidirectional_search(src, dest)

if out == -1:
  print(f"path does not exist between {src} and {dest}")