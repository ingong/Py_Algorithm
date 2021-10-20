# -*- coding: utf-8 -*-
graph = {'A':['B','C'],
         'B':['A','D','E'],
         'C':['A','H','G'],
         'D':['B'],
         'E':['B','F'],
         'F':['E'],
         'G':['C'],
         'H':['C']}

def dfs_iteration(graph, root):
    visited = []
    
    stack = [root]
    
    while(stack): 
        node = stack.pop() 
        if(node not in visited):
            visited.append(node)
            stack.extend(graph[node])
            
    return visited
 

def dfs_recursive(graph, start, visited=[]):
    visited.append(start) 
    
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited) 
    
    return visited


stack = dfs_iteration(graph,'A')
recursive = dfs_recursive(graph, 'A')

# 1. 재귀함수 vs Stack
# 재귀는 그래프의 연결된 노드의 앞부분부터 탐색
# stack 은 그래프의 연결된 노드위 뒷부분부터 탐색
# stack 에서는 extend 를 써야한다. 현재 그래프의 연결된 원소가 list 에 담겨있기 때문이다.

# 2. visited.append(node) vs visited = visisted + [node]
# 두 visited가 서로 다른 리스트를 참조하게 되므로
# 재귀 함수를 호출하면서 생기는 많은 함수들이
# 어떤 하나의 리스트에 모든 결과를 반영하는 것이 아니라
# 각자 독자적인 리스트를 갖게 되므로 저런 결과가 생기는 것.
# 만약 후자와 같은 방식을 취하고 싶다면 아래와 같은 방법으로 
# list 를 다시 할당해주는 방법이 있으나 비효율적인것같다


paths = []
graph1 = {'A':['B','C'],
         'B':['A','D','E'],
         'C':['A','F','G'],
         'D':['B'],
         'E':['B','H'],
         'F':['C','H'],
         'G':['C'],
         'H':['E','F']}

def dfs_paths(graph1, start, end, visited=[]):
    visited = visited + [start]
    
    if start == end:
        paths.append(visited)
    
    for node in graph1[start]:
        if node not in visited:
            dfs_paths(graph1, node, end, visited)

dfs_paths(graph1,'A','H')
print(paths)