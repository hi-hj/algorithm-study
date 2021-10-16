def replace_melody(melody):
    return melody.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

def solution(m, musicinfos):
    result = []
    m = replace_melody(m)
    
    for idx, info in enumerate(musicinfos):
        start, end, title, melody = info.split(',')
        sh, sm = start.split(':')
        eh, em = end.split(':')
        melody = replace_melody(melody)

        play_time = int(eh)*60 + int(em) - int(sh)*60 - int(sm)
        
        play = (melody * 1440)[:play_time]

        if m in play:
            result.append((play_time, idx, title))
    
    result.sort(key = lambda x: (-x[0], x[1]))

    if not result:
        return "(None)"
    return result[0][2]



solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])

















# def solution(m, musicinfos):
#     music_list = []
#     for i, music in enumerate(musicinfos):
#         start, end, name, info = music.split(',')
#         sh, sm = start.split(':')
#         eh, em = end.split(':')
#         play_len = int(eh)*60 + int(em) - int(sh)*60 - int(sm)
#         info = info.replace('C#','c')
#         info = info.replace('D#','d')
#         info = info.replace('F#','f')
#         info = info.replace('G#','g')
#         info = info.replace('A#','a')
        
#         ori_info = info
#         while len(ori_info) < play_len:
#             ori_info += info
#         ori_info = ori_info[:play_len]
#         music_list.append((play_len, i, name, ori_info))
    
#     m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    
#     music_list.sort(key = lambda x:(x[0],-x[1]), reverse = True)
    
#     answer = 0
#     for music in music_list:
#         if m in music[3]:
#             answer = music[2]
#             break
#     if answer ==0:
#         return '(None)'
#     return answer