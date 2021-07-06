def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: 3*x, reverse = True)
    result =''

    for n in numbers:
        result += n
    if int(result) == 0:
        return '0'
    else:
        return result

solution([3, 30, 34, 5, 9])












# def solution(numbers):
#     str_numbers = list(map(str, numbers))
#     str_numbers.sort(key = lambda x : 3*x, reverse=True)
#     result = ''
#     for n in str_numbers:
#         result +=n
#     if int(result) ==0:
#         return '0'
#     return result