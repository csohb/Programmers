
d=[1,3,2,5,4]
budget=9
def solution(d, budget):
    answer = 0
    sum=0
    for i in range(0, len(d)):
        sum+=int(d[i])
    
    d.sort()
    print(d)
    
    #필요한 금액보다 예산이 더 많을때
    if sum<budget:
        answer=len(d)  
    
    else:
        count=0
        while budget>0:
            budget-=d[count]
            count=count+1
            if not budget<0:
                answer=answer+1
            
        
    
    print(sum)
    print(answer)
    return answer

solution(d, budget)