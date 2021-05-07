


# Solution 1 (2021.05.08)
# DFS로 모든 경우 다 구하기 -> 부분집합 제거
# 코드가 길고 지저분, 최적화 방법 찾기
def check_key(relation, key):
    result = set()
    for i in range(row): # 모든 튜플 검색
        find = ''
        for j in key: # key 에 해당되는 column만
            find+=relation[i][j]
        result.add(find)
    if len(result) == row: # 모두 찾았으면, True 반환
        return True
    return False

def solution(relation):
    global row
    global answer
    answer = []
    column = len(relation[0])
    row = len(relation)

    def dfs(cur_idx, cur_list):
        global answer
        if cur_idx == column:
            if check_key(relation, cur_list):
                answer.append(set(cur_list))
            return
        
        dfs(cur_idx+1, cur_list)
        cur_list.append(cur_idx)
        dfs(cur_idx+1, cur_list)
        cur_list.pop()

    dfs(0,[])

    answer.sort(key= len)
    count = [True]*len(answer)
    for i in range(len(answer)):
        for j in range(i+1, len(answer)):
            if answer[j].issuperset(answer[i]):
                count[j] = False

    return sum(count)

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])