n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dust_ratio = [
    [
        [0,0,2,0,0],
        [0,10,7,1,0],
        [5,0,0,0,0],
        [0,10,7,1,0],
        [0,0,2,0,0]
    ],
    
    [
        [0,0,0,0,0],
        [0,1,0,1,0],
        [2,7,0,7,2],
        [0,10,0,10,0],
        [0,0,5,0,0]
    ],

    [
        [0,0,2,0,0],
        [0,1,7,10,0],
        [0,0,0,0,5],
        [0,1,7,10,0],
        [0,0,2,0,0]
    ],

    [
        [0,0,5,0,0],
        [0,10,0,10,0],
        [2,7,0,7,2],
        [0,1,0,1,0],
        [0,0,0,0,0]
    ]
]


x, y = n//2, n//2
move_dir = 0
move_num =1
dx = [0,1,0,-1] 
dy = [-1,0,1,0]


answer = 0
while True:
    
    for _ in range(move_num):
        x = x + dx[move_dir]
        y = y + dy[move_dir]   
        if x==0 and y==0:
            break
    if x==0 and y==0:
        break
    move_dir = (move_dir+1)%4
    if move_dir == 0 or move_dir ==2:
        move_num+=1