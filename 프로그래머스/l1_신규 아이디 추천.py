def solution(new_id):
    ID = list(new_id)
    
    # Step 1
    for idx, char in enumerate(ID):
        if char.isalpha():
            ID[idx] = char.lower()
    # Step 2
    s2 = []
    for char in ID:
        if char.isalpha() or char.isdigit() or char in ('-','_','.'):
            s2.append(char)
    # Step 3
    s3 = []
    for char in s2:
        if s3 and char =='.' and s3[-1]=='.':
            continue
        else:
            s3.append(char)
    
    # Step 4
    if s3[0] == '.':
        s3 = s3[1:]
    if s3 and s3[-1] == '.':
        s3 = s3[:-1]
    
    # Step 5
    if not s3:
        s3.append('a')

    # Step 6
    s3 = s3[:15]
    if s3[-1] =='.':
        s3 = s3[:-1]
    
    # Step 7
    while len(s3)<=2:
        s3.append(s3[-1])


    return ''.join(s3)



solution("...!@BaT#*..y.abcdefghijklm")
solution("=.=")