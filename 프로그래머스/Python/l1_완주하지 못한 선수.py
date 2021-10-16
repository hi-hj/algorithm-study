import collections

def solution(participant, completion):

    participant = collections.Counter(participant)
    completion = collections.Counter(completion)

    return list(participant-completion)[0]
    # print([participant-completion][0])
    # print(participant)
    # print(completion)




solution(["leo", "kiki", "eden"], ["eden", "kiki"])
solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])