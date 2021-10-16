def solution(n, k, cmd):
    answer = ['O'] * n
    idx = k
    
    erase_stack = []
    table = ['O'] * n

    for command in cmd:
        # print(command, table, erase_stack)
        # print(idx)
        if command[0]=='D':
            jump = int(command[2:])
            cnt = 0
            while cnt < jump:
                if table[idx+1] == 'O':
                    idx +=1
                    cnt +=1
                else:
                    idx +=1
        
        if command[0]=='U':
            jump = int(command[2:])
            cnt = 0
            
            while cnt < jump:
                # print(cnt, idx)
                if table[idx-1] == 'O':
                    idx -=1
                    cnt +=1
                else:
                    idx -=1
        
        if command[0] =='C':
            table[idx] = 'X'
            answer[idx] = 'X'
            erase_stack.append(idx)
            
            next_check = False
            
            while idx < n-1:
                if table[idx+1]=='O':
                    idx +=1
                    next_check = True
                    break
                idx +=1
            
            while next_check == False:
                if table[idx-1] =='O':
                    idx -=1
                    next_check = True
                    break
                idx -=1
        
        if command[0] =='Z':
            rollback_idx = erase_stack.pop()
            answer[rollback_idx] = 'O'
    
    return ''.join(answer)
    # print(answer)

            





# solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])