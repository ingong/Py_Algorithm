def solution(triangle):
    n = len(triangle)
    DP = [[0] * i for i in range(1, n+1)]
    
    DP[0][0] = triangle[0][0]
    for row in range(1, n):
        for column in range(0, row + 1):
            if column == 0: 
                upper_value = DP[row-1][column]
            elif column == row:
                upper_value = DP[row-1][column-1]
            else:
                upper_value = max(DP[row-1][column-1], DP[row-1][column])
            DP[row][column] = upper_value + triangle[row][column]
    
    return max(DP[-1])        
                