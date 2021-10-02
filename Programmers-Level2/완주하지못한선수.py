def create_dic(list):
    dic = {}
    for value in list:
        if value in dic:
            dic[value] += 1
        else:
            dic[value] = 1
    return dic

def solution(participant, completion):
    part_dic = create_dic(participant)
    complete_dic = create_dic(completion)    
    
    for key, value in part_dic.items():
        if (key not in complete_dic) or (complete_dic.get(key) != value):
            return key


# Counter 객체를 참고한 풀이 
1
2
3
4
5
6
7
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]