from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    time = 0
    now_weight = 0
    wait_truck = deque(truck_weights)

    while wait_truck:
        #돌리기
        down_truck = bridge.pop()
        bridge.appendleft(0)

        if down_truck !=0:
            now_weight -= down_truck
        #견딘다
        if now_weight + wait_truck[0] <= weight:
            truck = wait_truck.popleft()
            now_weight += truck
            bridge[0] = truck

        time +=1

        
        
        # print(bridge, wait_truck, now_weight, time)
    while bridge:
        bridge.pop()
        time +=1
    return time

solution(2, 10, [7,4,5,6])
solution(100,100,[10])
solution(100,100,[10,10,10,10,10,10,10,10,10,10])



















# import collections
# def solution(bridge_length, weight, truck_weights):
    
#     bridge = [0]*bridge_length
#     bridge = collections.deque(bridge)
#     truck_weights = collections.deque(truck_weights)
    
#     cnt = 0
#     sum_weight = 0

#     while truck_weights:
#         cnt +=1
#         # rotate
#         if bridge[-1] != 0:
#             sum_weight -= bridge[-1]
#         bridge.pop()
#         bridge.appendleft(0)
#         # new truck
#         if sum_weight + truck_weights[0] <= weight:
#             bridge[0] = truck_weights.popleft()
#             sum_weight += bridge[0]

#     return cnt+bridge_length