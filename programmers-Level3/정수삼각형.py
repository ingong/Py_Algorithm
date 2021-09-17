def solution(triangle):
    n = len(triangle)
    DP = [[0] * i for i in range(1, n+1)]
    
    DP[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(0, i + 1):
            if i == 0: 
                upper_value = DP[i-1][j]
            elif j == i:
                upper_value = DP[i-1][j-1]
            else:
                upper_value = max(DP[i-1][j-1], DP[i-1][j])
            DP[i][j] = upper_value + triangle[i][j]
    
    print(DP)        
                