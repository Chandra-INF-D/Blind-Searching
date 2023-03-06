def bfs(graph, source):
        visited = set()
        bfs_traversal = list()
        queue = list()

        queue.append(source)
        visited.add(source)

        while queue:
                current_node = queue.pop(0)
                bfs_traversal.append(current_node)

                for neighbour_node in graph[current_node]:
                        if neighbour_node not in visited:
                                visited.add(neighbour_node)
                                queue.append(neighbour_node)

        return bfs_traversal

def main():
        graph = {
                'A':['B','C'],
                'B':['A','D','E'],
                'C':['A','F','G'],
                'D':['B'],
                'E':['B'],
                'F':['C'],
                'G':['C']
        }
        bfs_traversal = bfs(graph,'A')
        print(f"BFS: {bfs_traversal}")

if __name__=='__main__':
       main()