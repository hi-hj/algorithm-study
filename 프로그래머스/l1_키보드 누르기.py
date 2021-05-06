def solution(numbers, hand):
    result = ''
    
    left = {1,4,7}
    right = {3,6,9}

    keypad = {1:(0,0), 4:(1,0), 7:(2,0), '*':(3,0),
             3:(0,2), 6:(1,2), 9:(2,2), '#':(3,2),
             2:(0,1), 5:(1,1), 8:(2,1), 0:(3,1)}
    
    now_left, now_right = '*', '#'
    
    for num in numbers:
        if num in left:
            result +='L'
            now_left = num

        elif num in right:
            result +='R'
            now_right = num
        
        else:
            num_point = keypad[num]
            left_point = keypad[now_left]
            right_point = keypad[now_right]

            num_to_left = abs(num_point[0] - left_point[0]) + abs(num_point[1]-left_point[1])
            num_to_right = abs(num_point[0] - right_point[0]) + abs(num_point[1]-right_point[1])
            

            if num_to_left < num_to_right or \
                (num_to_left == num_to_right and hand=='left'):
                result +='L'
                now_left = num

            elif num_to_left > num_to_right or \
                (num_to_left == num_to_right and hand=='right'):
                result +='R'
                now_right = num

    return result



solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right')