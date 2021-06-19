lottos=[0, 0, 0, 0, 0, 0]
win_nums=[38, 19, 20, 40, 15, 25]

def score(key):
    list={0:6,1:6,2:5,3:4,4:3,5:2,6:1}.get(key)
    return list

def solution(lottos, win_nums):
    answer = []
    zero=lottos.count(0)
    best=0
    worst=0
    match=0
    for i in win_nums:
        if i in lottos:
            match=match+1
            #print(match)
             
    best=match+zero
    worst=match
    
    best=score(best)
    worst=score(worst)
    print(f'best={best}')
    print(f'worst={worst}')
    
    
    
    answer.extend([best,worst])
    print(answer)
    return answer

solution(lottos, win_nums)



