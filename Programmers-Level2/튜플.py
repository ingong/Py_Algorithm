def solution(s):
    s = s[2:-2].split('},{')
    
    dic = {}
    for number in s:
        dic[number.count(',')] = number.split(',')
    
    answer = []
    for _, value in sorted(dic.items()):
        for number in value: 
            if not number in answer:
                answer.append(number)
    
    return [int(v) for v in answer]