import sys

T = int(input())

def Manhattan(x, y, points):
    calc = 0
    for x1,y1,x2,y2 in points:
        if x1<=x<=x2:
            pass
        else:
            calc += min(abs(x-x1), abs(x-x2))
        
        if y1<=y<=y2:
            pass
        else:
            calc += min(abs(y-y1), abs(y-y2))
    return calc

for tc in range(1, T+1):
    K = int(input())
    points = []
    answers = []
    distacne = sys.maxsize


    x = []
    y = []

    for _ in range(K):
        point = list(map(int, input().split()))
        x.append(point[0])
        x.append(point[0])
        x.append(point[2])
        x.append(point[2])

        y.append(point[1])
        y.append(point[1])
        y.append(point[3])
        y.append(point[3])
    
    # print(x, y)
    x.sort()
    y.sort()


    answer = "Case #"+str(tc)+": "+str(x[((K*4+1)//2)-1])+" "+str(y[((K*4+1)//2)-1])
    print(answer)



    

# import sys

# T = int(input())

# def Manhattan(x, y, points):
#     calc = 0
#     for x1,y1,x2,y2 in points:
#         if x1<=x<=x2:
#             pass
#         else:
#             calc += min(abs(x-x1), abs(x-x2))
        
#         if y1<=y<=y2:
#             pass
#         else:
#             calc += min(abs(y-y1), abs(y-y2))
#     return calc

# for tc in range(1, T+1):
#     K = int(input())
#     points = []
#     answers = []
#     distacne = sys.maxsize

#     mx,my,Mx,My = sys.maxsize, sys.maxsize, -sys.maxsize, -sys.maxsize


#     for _ in range(K):
#         point = list(map(int, input().split()))
#         mx = min(mx, point[0])
#         my = min(my, point[1])
#         Mx = max(Mx, point[2])
#         My = max(My, point[3])
#         points.append(point)
    
    
#     for x in range(mx, Mx+1):
#         for y in range(my, My+1):
#             now = Manhattan(x,y,points)
#             # print(x,y,now, answers)

#             if now < distacne:
#                 distacne = now
#                 ax = x
#                 ay = y

    
    
#     answer = "Case #"+str(tc)+": "+str(ax)+" "+str(ay)
#     print(answer)
    