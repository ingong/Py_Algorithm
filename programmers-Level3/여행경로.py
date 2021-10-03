from collections import defaultdict

def solution(tickets):
    path = defaultdict(list)
    
    for dep, arr in tickets:
        path[dep].append(arr)
    
    for key in path.keys():
        path[key].sort(reverse = True)
    
    stack = ['ICN']
    routes = []
    while stack:
        top = stack[-1]
        if path[top] == []:
            routes.append(stack.pop())
        else:
            stack.append(path[top].pop())
            
    
    return routes[::-1]
        