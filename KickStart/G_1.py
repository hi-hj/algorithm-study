T = int(input())


for tc in range(1, T+1):
    N, D, C, M = map(int, input().split())

    animals = list(input())
    portion = {'D':D, 'C':C}
    count = animals.count('D')
 
    for animal in animals:
        if count ==0:break
        # Dog
        if animal=='D':
            if portion[animal]>0:
                portion['D']-=1
                portion['C']+=M
                count-=1
            else:
                break
        # Cat
        elif animal=='C':
            if portion[animal]>0:
                portion['C']-=1
            else:
                break
    answer = "Case #"+str(tc)
    if count==0:
        answer+=": YES"
        print(answer)
    else:
        answer+=": NO"
        print(answer)

