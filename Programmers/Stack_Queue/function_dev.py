import math 

progresses=[95, 90, 99, 99, 80, 99]
speeds=[1, 1, 1, 1, 1, 1]
def solution(progresses, speeds):
    
    '''
        작업이랑 스피드를 전부 계산해줌 -> 100% 될때까지
        각각 며칠 걸리는지 따져봄 -> 배열에 담음
        맨 앞부터 따져봄 0보다 1이 작으면 기다려야함 
        그 다음 큰 수까지 기다리고 나머지도 기다려야함
    '''
    done=[] #걸리는 시간
    for i in range(0, len(progresses)):
        print(progresses[i])
        done.append(math.ceil((100-progresses[i])/speeds[i]))
    
    print(done) #[7, 3, 9]
    '''
        기준이 되는 날짜를 정하고 그 뒤에 숫자를 하나씩 비교해줌
        비교날짜 - 다음날짜 < 0 일때까지
        2차원배열 사용?
        [[1,2,3],[4,5],[6,7,8]] 이런식으로 넣어준 다음
        각각의 len 구해서 answer배열에 넣어줌
    '''
    answer = [[0 for col in range(len(done))] for row in range(len(done))]
    
    st=0 #기준날짜
    count=0 #몇번째 기준날짜인지
    answer[count].append(done[0])
    for i in range(1, len(done)):
        st=done[0] #첫번째 
        
        if st - done[i] < 0:
            count+=1
            st=done[i]
            answer[count].append(st)
            
            
        elif st - done[i] == 0:
            answer[count].append(done[i])
            
        elif st - done[i] > 0:
            answer[count].append(done[i])
            
    
    
    print(answer)    
     
     
           
        
    
    return answer
solution(progresses, speeds)