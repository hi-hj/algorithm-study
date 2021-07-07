def solution(number, k):
    answer = ''
    stack = []

    for n in number:
        while k >0:
            if stack and n > stack[-1]:
                stack.pop()
                k -=1
            else:
                break
        stack.append(n)
        print(n, stack)
solution('4177252841', 4)



# import collections
# def solution(number, k):
#     stack = collections.deque()
    
#     for n in number:
#         while k>0:
#             if stack and n > stack[-1]:
#                 stack.pop()
#                 k-=1
#             else:
#                 break
#         stack.append(n)
    
#     result = ''.join(stack)
#     if k>0:
#         result = result[:-k]

#     return result