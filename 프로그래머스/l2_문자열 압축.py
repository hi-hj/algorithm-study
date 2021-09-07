def solution(s):

    if len(s)==1:
        return 1

    result = []
    
    for i in range(1, (len(s)//2)+1):
        newS = ''
        cnt = 1
        before = s[0:i]
        j = i

        while j < len(s):
            now = s[j:j+i]

            if before == now:
                cnt+=1
            elif before != now and cnt ==1:
                newS += before
                before = now
                cnt = 1
            elif before != now:
                newS = newS +str(cnt)+before
                before = now
                cnt = 1

            if j+i >=len(s):
                if before == s[j:]:
                    if cnt ==1:
                        newS = newS + before
                    else:
                        newS = newS + str(cnt) + before
                
                else:
                    newS += s[j:]
            j+=i
        

        result.append(newS)


    for idx, val in enumerate(result):
        result[idx] = len(val)

    return min(result)


solution('a')
# solution("aabbaccc")
# solution("ababcdcdababcdcd")
# solution("abcabcdede")