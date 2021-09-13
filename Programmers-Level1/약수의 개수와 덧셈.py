def division(x):
    count = 0
    
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    
    return count
        
def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if division(num) % 2 == 0:
            answer += num
        else:
            answer -= num
            
    return answer