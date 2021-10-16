def solution(files):
    sorted_files = []
    
    for i, f in enumerate(files):
        start_n, end_n = -1, -1

        for ni, nn in enumerate(f):
            if start_n ==-1 and nn.isdigit():
                start_n = ni
            
            if ni==len(f)-1 or (nn.isdigit() and not f[ni+1].isdigit()):
                end_n = ni
                break
        # print(f, start_n, end_n)

        head = f[:start_n]
        number = f[start_n: end_n+1]
        tail = f[end_n+1:]

        # print(head, number, tail)

        sorted_files.append((head.lower(), int(number), i, head, number, tail))
    sorted_files.sort(key = lambda x:(x[0], x[1], x[2]))

    # print(sorted_files)
    result = []

    for _, _, _, head, number, tail in sorted_files:
        result.append(head + number+tail)

    return result

    print(result)



solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
# solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])







# def solution(files):
#     sorted_files = []
#     for i, file in enumerate(files):
#         origin_head = ''
#         head_write = True
#         origin_num = ''
#         num_write = False
#         tail = ''
#         tail_write = False
#         for f in file:
#             if head_write:
#                 if f.isdigit():
#                     head_write = False
#                     num_write = True
#                     origin_num +=f
#                 else:
#                     origin_head +=f
#             elif num_write:
#                 if not f.isdigit():
#                     num_write = False
#                     tail_write = True
#                     tail +=f
#                 else:
#                     origin_num +=f
#             else:
#                 tail+=f
#         head = origin_head.lower()
#         num = int(origin_num)
        
#         sorted_files.append([head, num, i, origin_head, origin_num, tail])
    
#     sorted_files.sort(key = lambda x : (x[0], x[1], x[2]))
#     result = []
#     for file in sorted_files:
#         result.append(''.join((file[3],file[4],file[5])))
        
#     return result