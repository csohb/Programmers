#완주하지 못한 선수

# 효율성 떨어짐
'''
def solution(participant, completion):
    answer = ''
    for i in completion:
        if i in participant:
            participant.remove(i)
    answer+=participant[0]
    return answer
'''
# 효율성 통과
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p!=c:
            return p
    return participant[-1]

'''
    zip 함수 => 튜플로 앞에서부터 짝지어줌
    참가자 명단에 있지만 완주자 명단에 없는 선수
    or
    짝지어지지 않은 마지막 선수 리턴
'''
