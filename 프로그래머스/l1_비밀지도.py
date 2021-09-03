import pprint

def solution(n, arr1, arr2):
    arr = [[' ']*n for _ in range(n)]
    # pprint.pprint(arr)
    
    for i, num in enumerate(arr1):
        bin_num = bin(num)[2:].zfill(n)
        for j, bn in enumerate(bin_num):
            if bn == '1':
                arr[i][j] = '#'
    
    for i, num in enumerate(arr2):
        bin_num = bin(num)[2:].zfill(n)
        for j, bn in enumerate(bin_num):
            if bn == '1':
                arr[i][j] = '#'
    


    for i in range(n):
        arr[i] = ''.join(arr[i])

    pprint.pprint(arr)



    return arr





solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
# solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])