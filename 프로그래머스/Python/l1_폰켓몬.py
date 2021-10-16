from collections import Counter

def solution(nums):
    count = Counter(nums)
    max_num = len(nums)//2
    answer = 0
    for num in count:
        if answer >= max_num:
            break
        answer +=1
    return answer

    # return min(len(ls)/2, len(set(ls)))

solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])