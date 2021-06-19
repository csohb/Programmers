from multiprocessing.connection import answer_challenge
n=45

def solution(n):
    answer=''
    
    while n>0:
        n,remain=divmod(n, 3)
        answer+=str(remain)
        
   
    answer=int(answer,3)
    print(answer)
    return(answer)    
solution(n)