def check_build(build):

    for x,y,a in build:

        # 기둥
        if a == 0:
            # 바닥위가 아니고 and
            # 보의 한쪽 끝 위에도 없고 and
            # 다른 기둥 위에도 없다면
            # return True
            if y!=0 and \
                ([x,y,1] not in build and [x-1,y,1] not in build) and \
                [x,y-1,0] not in build:
                return True
        # 보
        elif a == 1:
            # 양쪽 끝이 기둥위에 없고 and
            # 양쪽 끝 다른 보와 연결되지 않았을 때 (둘다 있어야 하므로 or)
            if ([x,y-1,0] not in  build and [x+1,y-1,0] not in build) and \
                ([x-1,y,1] not in build or [x+1,y,1] not in build):
                return True
    return False


def solution(n, build_frame):
    result = []
    
    for x,y,a,b in build_frame:
        # 설치
        if b == 1:
            result.append([x,y,a])
            
            if check_build(result): # 설치가 불가능하다면
                result.remove([x,y,a]) # 다시 뺀다
        
        # 삭제
        elif b == 0:
            result.remove([x,y,a])

            if check_build(result): # 삭제가 불가능하다면
                result.append([x,y,a]) # 다시 더한다

    result.sort()
    return result




solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])