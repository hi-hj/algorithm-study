def solution(numbers, hand):
    left ={1:(0,0),4:(1,0),7:(2,0)}
    right = {3:(0,2),6:(1,2),9:(2,2)}
    middle = {2:(0,1),5:(1,1),8:(2,1),0:(3,1)}
    
    left_now = (3,0)
    right_now = (3,2)

    answer = ''
    
    for number in numbers:
        if number in left:
            answer +='L'
            left_now = left[number]
        elif number in right:
            answer +='R'
            right_now = right[number]
        else:
            left_cnt = abs(left_now[0]-middle[number][0]) + abs(left_now[1]-middle[number][1])
            right_cnt = abs(right_now[0]-middle[number][0]) + abs(right_now[1]-middle[number][1])

            if left_cnt < right_cnt or (left_cnt==right_cnt and hand=='left'):
                answer +='L'
                left_now = middle[number]
            elif left_cnt > right_cnt or (left_cnt==right_cnt and hand=='right'):
                answer +='R'
                right_now = middle[number]
    return answer


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")