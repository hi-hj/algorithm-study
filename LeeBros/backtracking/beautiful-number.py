n = int(input())

numbers = [1, 2, 3, 4]


def check_beautiful(number):
    n_cnt = 1
    n_check = []
    for i in range(len(number)):
        if i==len(number)-1 or number[i] == n_cnt or number[i]!=number[i+1]:
            n_check.append((number[i], n_cnt))
            n_cnt = 1
        elif number[i] == number[i+1]:
            n_cnt +=1
            
    for num, cnt in n_check:
        if num !=cnt:
            return False
    return True

cnt = 0
def make_numbers(cur_idx, n, number):
    global cnt
    if cur_idx == n:
        if check_beautiful(number):
            cnt +=1
        return
    
    for i in range(4):
        number.append(numbers[i])
        make_numbers(cur_idx+1, n, number)
        number.pop()
    
make_numbers(0, n, [])



print(cnt)