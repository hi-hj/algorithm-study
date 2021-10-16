from itertools import combinations
from collections import Counter, defaultdict

def solution(orders, course):
    result = []
    count = Counter()
    
    # 1. Count All case
    for order in orders:        
        for num in course:
            count += Counter(list(combinations(sorted(order),num)))

    # 2. Calc Max Case
    max_menu = defaultdict(int)
    for key, val in count.items():
        max_menu[len(key)] = max(max_menu[len(key)], val)
    
    # 3. Find Answer
    result = []
    for key, val in count.items():
        if val!=1 and val == max_menu[len(key)]:
            result.append(''.join(key))
    
    # 4. Sort Answer
    result.sort()
    return result
    

# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])