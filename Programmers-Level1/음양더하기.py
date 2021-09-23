def solution(absolutes, signs):
    return sum([number if signs[index] else -number for index, number in enumerate(absolutes)])