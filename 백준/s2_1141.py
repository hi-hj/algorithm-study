n = int(input())
words = []
for i in range(n):
    words.append(input())
words.sort(key = len)

answer = 0
# print(words)
for i in range(n-1):
    now_word = words[i]
    for j in range(i+1,n):
        next_word = words[j]
        if next_word.startswith(now_word):
            # print(now_word, next_word)
            answer +=1
            break
            
print(n-answer)

# def define_list(words):
#     for i in range(len(words)-1):
#         now_word = words[i]
#         for j in range(i+1, len(words)):
#             next_word = words[j]
#             if next_word.startswith(now_word):
#                 return False    
#     return True


# print(answer)


