def solution(left, right):
    double_num = [i for i in range(1, 32)]
    for idx, num in enumerate(double_num):
        double_num[idx] = num **2


    answer = 0

    for num in range(left, right+1):
        if num in double_num:
            answer -= num
        else:
            answer += num
    return answer
solution(13, 17)