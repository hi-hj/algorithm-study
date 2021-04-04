import collections
n = int(input())

see = ['1']
now = 0

while now < n:
    # '1' , '11'
    n_text = see[now]
    see_list = collections.deque()
    result = ''
    cnt = 0
    print(n_text)

    for i in range(0, len(n_text)):
        print(n_text[i], n_text[i-1])
        if n==0:
            cnt +=1
        elif n_text[i]==n_text[i-1]:
            cnt +=1
            if i==len(n_text)-1:
                see_list.appendleft((n_text[i-1], cnt))
        elif n_text[i]!=n_text[i-1]:
            see_list.appendleft((n_text[i-1], cnt))
            cnt = 1
            if i==len(n_text)-1:
                see_list.appendleft((n_text[i], cnt))
    print(see_list)

    for i, v in see_list:
        result += str(i) + str(v)
    see.append(result)
    now +=1

print(see)
    





# def make_list(n):
#     now = 1
#     # see_say[n]을 도출할때까지 지속
#     # see_say[0] -> see_say[1] --... > see_say[n]
#     while now < n:
#         see_list = []
#         result = ''
#         print(len(see[now-1]), see[now-1])
#         for i in range(len(see[now-1])):
#             # 시작
#             if i==0:
#                 cnt = 1
            
#             elif see[now-1][i]!=see[now-1][i-1]:
#                 see_list.append((see[now-1][i-1], cnt))
#                 cnt = 1
#             elif see[now-1][i]==see[now-1][i-1]:
#                 cnt +=1

#             # 끝
#             if i==len(see[now-1])-1:
#                 see_list.append((see[now-1][i], cnt))
        
#         print(see_list)
        
#         for i, v in see_list:
#             result += str(i)+str(v)
#         see.append(result)

#         now +=1
    
#     print(see)
        
# make_list(2)
