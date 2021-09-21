answer = 0
def DFS(L, total, numbers, target):
    global answer
    if L == len(numbers):
        if total == target:
            answer += 1
        else:
            return
    else:
        DFS(L + 1, total + numbers[L], numbers, target)
        DFS(L + 1, total - numbers[L], numbers, target)
        

def solution(numbers, target):    
    global answer
    DFS(0, 0, numbers, target)
    return answer
