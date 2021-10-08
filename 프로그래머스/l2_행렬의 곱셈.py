def solution(arr1, arr2):
    a = len(arr1)
    b = len(arr1[0])
    c = len(arr2[0])
    
    answer = [[0]*c for _ in range(a)]
    
    for i in range(a):
        for j in range(c):
            for k in range(b):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer