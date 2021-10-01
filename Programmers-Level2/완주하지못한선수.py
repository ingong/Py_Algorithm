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
        