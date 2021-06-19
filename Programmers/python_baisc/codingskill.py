A=[-100000,-3]

def solution(A):
    answer=0
    '''
        배열에 없으면서 가장 작은 수를 구하라
        -> 배열이 다 마이너스면 무조건 1
        -> 배열의 가장 큰 수, 작은 수 구하기
        -> 그 중에 없는 수 구하기
         --- 이걸 어떻게 할 것인가
         큰수부터 작은수까지 있는 배열을 만들고 그 중에서 A에 없는 숫자들을 temp2에 담음
         -> 그러고 나서 거기서 제일 작은수를 리턴하면됨
         -> 만약에 temp2의 길이가 0이다 그러면 그냥 Max에 +1
        
        -> 여기서 가장 작은 수 return 
        -> 없는 수가 없으면 가장 큰 수 +1
    '''
    
    
    
    small=min(A)
    big=max(A)
    if big < 0:
        answer=1
        print(answer)
        return answer
    
    nums=list(range(small, big+1))
    aList=[]
    for i in nums:
        if i not in A:
            aList.append(i)
    
    if len(aList) > 0:
        answer=min(aList)
        if answer==0:
            answer=1
    else:
        answer=big+1
    
    print(answer)
    return answer
            
solution(A)
    
        