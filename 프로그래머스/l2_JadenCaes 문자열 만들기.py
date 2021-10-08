def solution(s):
    s = s.lower()
    s = s.split(' ')
    print(s)
    for i in range(len(s)):
        s[i] = s[i].capitalize()  

    return ' '.join(s)