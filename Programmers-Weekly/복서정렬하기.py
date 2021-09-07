arr = []

def make_std(weights, head2head):
    global arr
    n = len(weights)
    for i in range(n):
        rate = 0
        win = 0
        lose = 0
        heavy_win = 0
        
        for j in range(n):
            if i == j: continue
            if head2head[i][j] == 'L': lose += 1
            elif head2head[i][j] == 'W':
                win += 1
                if weights[i] < weights[j]: heavy_win += 1
            
        rate = win * 100 / (win + lose) if win + lose != 0 else 0
        arr.append([-rate, -heavy_win, -weights[i], (i+1)])
        
def solution(weights, head2head):
    global arr
    make_std(weights, head2head)
    arr.sort()
    answer = [x[-1] for x in arr]
    return answer