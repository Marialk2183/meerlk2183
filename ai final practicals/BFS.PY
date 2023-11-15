graph = {
'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A', 'F'],
'D': ['B'],
'E': ['B', 'F'],
'F': ['C', 'E']
 }
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
       vertex = queue.popleft()
       if vertex not in visited:
          visited.add(vertex)
          print(vertex)
# Explore neighbors
          neighbors = graph[vertex]
          for neighbor in neighbors:
              if neighbor not in visited:
                  queue.append(neighbor)
# Example usage

start_vertex = 'A'
print("following is bfs:")
bfs(graph, start_vertex)
