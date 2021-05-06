#Lv4 2019 겨울 인턴십
#호텔 방 배정
 
def solution(k, room_number):
    answer = []
    #체크용 딕셔너리
    room = {}
    #손님을 받으며 체크하자
    for num in room_number:
        #딕셔너리에 확인 0이라면 배정이 안됬고, 다른값이 있다면 이미 배정되었다.
        number = room.get(num, 0)
        if number :
            #임시변수에 방번호를 넣어준다,
            temp = [num]
            #반복문을 돌면서 빈방이 나올때까지 체크
            while True:
                index = number
                #이동했던 위치를 이용하여 다시 이동
                number = room.get(number, 0)
                #방이 비어있다면 방을 할당
                if not number:
                    #정답에 추가해주고
                    answer.append(index)
                    #딕셔너리에 값을 등록하고
                    room[index] = index + 1
                    #이전에 거쳤던 방들도 바꿔준다.
                    for i in temp:
                        room[i] = index + 1
                    break
                temp.append(number)
        #배정이 안되어있다면 결과추가하고 방배정 되었다고 딕셔너리에 표시
        else:
            answer.append(num)
            room[num] = num + 1
    return answer






# 정확성 O , 효율성 X
# def solution(k, room_number):
#     result = []
#     full = set()

#     for num in room_number:
#         while num in full:
#             num+=1
#         result.append(num)
#         full.add(num)
#     return result



k = 10
room_number = [1,3,4,1,3,1]
solution(k, room_number)