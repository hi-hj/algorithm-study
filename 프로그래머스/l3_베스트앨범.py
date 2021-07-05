from collections import defaultdict

def solution(genres, plays):
    many_genre = defaultdict(list)
    answer = []
    
    for i in range(len(genres)):
        many_genre[genres[i]].append((plays[i], i))
    print(many_genre)

    grade_genre = []
    
    for g in many_genre:
        sum_play = 0
        for num, _ in many_genre[g]:
            sum_play += num
        grade_genre.append((sum_play, g))
    grade_genre.sort(key = lambda x:x[0], reverse=True)
    print(grade_genre)

    for g in many_genre:
        many_genre[g].sort(key= lambda x:x[0], reverse=True)
    print(many_genre)

    for _, g in grade_genre:
        answer.append(many_genre[g][0][1])

        if len(many_genre[g])>1:
            answer.append(many_genre[g][1][1])
    
    return answer




# import collections

# def solution(genres, plays):
#     answer = []
#     mix_genre = collections.defaultdict(list)
#     grade_genre = []


#     for i in range(len(plays)):
#         mix_genre[genres[i]].append((plays[i], i))
    
#     print(mix_genre)


#     for g in mix_genre:
#         sum_play = 0
#         for num, _ in mix_genre[g]:
#             sum_play += num
#         grade_genre.append((sum_play, g))
    
#     print(grade_genre)


#     grade_genre.sort(key = lambda x : x[0], reverse=True)
#     print(grade_genre)
#     for g in mix_genre:
#         mix_genre[g].sort(key = lambda x : (-x[0], x[1]))
    
#     print(mix_genre)

#     for _, g in grade_genre:
        
#         answer.append(mix_genre[g][0][1])
#         if len(mix_genre[g])>1:
#             answer.append(mix_genre[g][1][1])
    
        
#     return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])