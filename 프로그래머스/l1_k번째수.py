def solution(array, commands):
    answer = []

    for command in commands:
        cut_array = array[command[0]-1:command[1]]
        cut_array.sort()
        answer.append(cut_array[command[2]-1])

    return answer


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])











# def solution(array, commands):
#     result = []
#     for i, j, k in commands:
#         result.append(sorted(array[i-1:j])[k-1])
#     return result