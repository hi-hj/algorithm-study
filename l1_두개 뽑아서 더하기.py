# https://programmers.co.kr/learn/courses/30/lessons/68644
# 프로그래머스 > 월간 코드 챌린지 시즌 1
# 두개 뽑아서 더하기 (Level 1)

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            result = numbers[i] + numbers[j]
            if result not in answer:
                    answer.append(result)
    answer.sort()
    print(answer)
    return answer

