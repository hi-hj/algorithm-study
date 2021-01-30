def ant_numbers(number):
    str_num = ''
    count = 1
    for idx in range(0, len(number)):
        if(idx+1 == len(number)) or number[idx]!=number[idx+1]:
            str_num += str(number[idx]) + str(count)
            count = 1
        else:
            count += 1
    return str_num



num = int(input())
start = '1'

for i in range(0, num-1):
    start = ant_numbers(start)

print(start)
