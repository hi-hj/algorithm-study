import pprint
from collections import defaultdict

def solution(table, languages, preference):
    
    job_score = defaultdict(list)
    scores = [0]*5
    for score in table:
        texts = score.split()
        JOB = texts[0]
        job_score[JOB]+= reversed(texts[1:6])
    

    for idx, job in enumerate(job_score):
        scoe = 0
        for language, pre in zip(languages, preference):
            if language in job_score[job]:
                get_score = job_score[job].index(language) + 1
            else:
                get_score = 0
            scores[idx] += (get_score * pre)
    
    max_score = max(scores)
    answer = []
    for idx, job in enumerate(job_score):
        if scores[idx] == max_score:
            answer.append(job)
    
    answer.sort()
    return answer[0]






    


solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], 	[7, 5, 5])


solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["JAVA", "JAVASCRIPT"],[7,5])