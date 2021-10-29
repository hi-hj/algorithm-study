import sys
T = int(input())


def back_tracking(cur_idx, one, two, total):
    global answer

    if total > K or len(one)+len(two)>answer:
        return
    if total == K:
        answer = min(answer, len(one)+len(two))
        return
    if cur_idx == len(banana):
        return

    # 1. One
    if not one or (one[-1]+1==cur_idx):
        one.append(cur_idx)
        total += banana[cur_idx]
        back_tracking(cur_idx+1, one, two, total)
        one.pop()
        total -= banana[cur_idx]
    
    # 2. Two
    if (one and one[-1]+1!=cur_idx) and (not two or two[-1]+1==cur_idx):
        two.append(cur_idx)
        total += banana[cur_idx]
        back_tracking(cur_idx+1, one, two, total)
        two.pop() 
        total -= banana[cur_idx]
    
    # 3. Pass
    back_tracking(cur_idx+1, one, two, total)


K = 0
banana = []
answer = 0

for tc in range(1, T+1):
    N, K = map(int, input().split())
    banana = list(map(int, input().split()))

    answer = sys.maxsize

    back_tracking(0,[],[],0)

    string = "Case #"+str(tc)+": "
    if answer == sys.maxsize:
        string += "-1"
    else:
        string += str(answer)
    
    print(string)

    
    
    