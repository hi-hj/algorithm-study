def solution(n, words):
    check = set()
    index = 0
    last = ''
    answer = (0,0)
    for word in words:
        # print(last, word)
        if word in check or (len(last)>0 and last[-1]!=word[0]):
            index +=1
            # print(index)
            answer = divmod(index, n)
            break
        else:
            check.add(word)
            index +=1
            last = word
    
    a,b = answer
    if b==0 and (a,b)!=(0,0):
        b = n
    elif (a,b)!=(0,0):
        a +=1
    return [b,a]

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])
solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])