from collections import Counter
def solution(str1, str2):
    
    count1 = []
    count2 = []
    # 1. 영어만 처리 + 소문자로 + 2개씩 끊어서
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            count1.append(str1[i].lower() + str1[i+1].lower())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            count2.append(str2[i].lower() + str2[i+1].lower())
    
    # 2. 합집합 & 교집합
    count1 = Counter(count1)
    count2 = Counter(count2)

    share = count1 & count2
    union = count1 | count2

    share_num = 0
    union_num = 0

    for key, count in share.items():
        share_num += count
    for key, count in union.items():
        union_num += count

    # 4. 계산하기
    if union_num == 0:
        return 65536
    answer = int((share_num / union_num) * 65536)
    return answer

solution('handshake', 'shake hands')
solution('aa1+aa2','AAAA12')

# solution("FRANCE", "french")
# solution("E=M*C^2", "e=m*c^2")