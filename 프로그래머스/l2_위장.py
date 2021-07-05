from collections import defaultdict

def solution(clothes):
    answer = 1

    cloth_list = defaultdict(list)
    for val, key in clothes:
        cloth_list[key].append(val)

    for key in cloth_list:
        answer *= (len(cloth_list[key])+1)
    
    return answer-1


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])