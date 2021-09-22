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
  
# 프로그래머스 다른 사람 풀이 참고
# 약수의 개수의 합과 유사, 시간 초과제한이 있었던 약수의 합 문제와 유사함
# 모든 문자열에서 본인이 해당하는 개수를 Counter 로 센 이후에 개수가 적은 순으로 정렬
# list(map(int, list)) 를 통해서 모두 정수형으로 변환함
import re
from collections import Counter
def solution(s):
    s = Counter(re.findall('\d+', s))
    print(s)
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

