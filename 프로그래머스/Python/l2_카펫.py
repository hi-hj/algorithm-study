def solution(brown, yellow):
    sqaure = brown + yellow
    
    can_make = []
    
    print(sqaure)
    for a in range(1, int(sqaure**(1/2)+1)):
        b, check = divmod(sqaure, a)
        if check == 0:
            can_make.append((b, a))
    print(can_make)
    
    for a, b in can_make:
        print(a, b, brown)
        if 2*(a+b-2) == brown:
            print(a, b)
            return [a,b]

solution(10,2)



# def solution(brown, yellow):
#     can_make = []
#     all_by = brown+yellow
#     for i in range(3, int((all_by)**0.5)+1):
#         if (all_by) % i ==0:
#             can_make.append((all_by//i, i))
#     for m, n in can_make:
#         if (m-2)*(n-2) == yellow:
#             return [m,n]