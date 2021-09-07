from collections import defaultdict

def solution(record):
    print(record)
    names = defaultdict()
    
    messages = []
    
    for message in record:
        message = list(message.split())
        # print(message)

        if message[0] == 'Enter':
            messages.append(('들어왔습니다.',message[1]))
            names[message[1]] = message[2]
        elif message[0] == 'Change':
            names[message[1]] = message[2]
        elif message[0] == 'Leave':
            messages.append(('나갔습니다.', message[1]))
    
    # print(messages)
    # print(names)
    
    result = []
    for action, uid in messages:
        result.append(names[uid]+'님이 '+action)
    print(result)


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])



# from collections import defaultdict

# def solution(record):
#     name = defaultdict(str)
#     result = []

#     for log in record:
#         log = log.split()

#         if log[0] == 'Enter':
#             name[log[1]] = log[2]
#             result.append((log[0], log[1]))

#         elif log[0] =='Leave':
#             result.append((log[0],log[1]))

#         elif log[0] =='Change':
#             name[log[1]] = log[2]


#     answer = []


#     for action, uid in result:    
#         console = name[uid]+'님이 '
        
#         if action=='Enter':
#             console +='들어왔습니다.'
        
#         elif action=='Leave':
#             console +='나갔습니다.'
        
#         answer.append(console)
    
#     return answer

# solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])