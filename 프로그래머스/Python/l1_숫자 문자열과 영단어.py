def solution(s):
    numbers = {'zero':'0', 'one':'1', 'two':'2','three':'3', 'four':'4',
                'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
        
    for string, number in numbers.items():
        while string in s:
            s = s.replace(string, number)
    print(int(s))
    return int(s)


solution("one4seveneight")
solution("23four5six7")
solution("2three45sixseven")
solution("123")