from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    
    count, cache = 0,deque()
    for city in cities:
        city = city.lower()
        
        if city in cache:
            count += 1
            cache.remove(city)
            cache.append(city)
        else:
            count += 5
            cache.append(city)
            if cacheSize < len(cache):
                cache.popleft()
                
    return count