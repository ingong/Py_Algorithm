import re

def solution(files):
    temp = [re.split("([\d]+)", s) for s in files]
    sorted_list = sorted(temp, key = lambda x : (x[0].lower(), int(x[1])))
    
    return [("").join(v) for v in sorted_list]