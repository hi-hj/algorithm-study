from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    time = 0

    # Edge Case
    if cacheSize == 0:
        return len(cities)*5
    

    for city in cities:
        city = city.lower()
        
        # HIT
        if city in cache:
            time +=1
            cache.remove(city)
            cache.append(city)
        
        # MISS
        elif city not in cache:
            time +=5
            if len(cache) == cacheSize:
                cache.popleft()
                cache.append(city)
            else:
                cache.append(city)
    
    return time
    

solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])




# import collections

# def solution(cacheSize, cities):
#     cache = collections.deque()
#     print(cache)
#     cnt = 0
#     if cacheSize == 0: return len(cities)*5
    
#     for citi in cities:
#         citi = citi.lower()
#         # CACHE MISS
        
#         if citi not in cache:
#             cnt +=5
#             if len(cache) == cacheSize:
#                 cache.popleft()
#                 cache.append(citi)
#             else:
#                 cache.append(citi)
        
        
#         else:
#             cnt +=1
#             cache.remove(citi)
#             cache.append(citi)
#     return cnt