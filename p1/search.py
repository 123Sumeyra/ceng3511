from collections import defaultdict
import sys

graph = defaultdict(list)
argv= sys.argv
def add_Edge(graph, u, v):
    graph[u].append(v)



with open("C:\Users\asus\Desktop\python", 'r') as file

    for i in file :
        pass


def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def dfs(graph, start):
    visited = set()
    stack =[start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
        print(stack)
    return visited




start_state = str(input("Please enter the start state : "))
goal_state = str(input("Please enter the goal state : "))


start_state = start_state.upper
goal_state = goal_state.upper

