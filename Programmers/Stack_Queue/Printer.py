priorities=[2, 1, 3, 2]
location=2
'''
    가장 앞에 있는 문서를 꺼낸다
    뒤에 있는 항목과 비교 꺼낸것 가장 뒤로보냄
    아니면 j인쇄
    
    location은 찾고 싶은 인덱스 번호
'''
def solution(priorities, location):
    answer = 0
    count=0
    
    while (len(priorities)):
        #찾을 인덱스가 0번이면
        if location==0:
            #찾으려는 수가 배열의 가장 큰수보다 작으면
            if priorities[0]<max(priorities):
                #배열 맨 뒤에 숫자를 넣음
                priorities.append(priorities.pop(0))
                #인덱스를 맨뒤에 맞게 설정
                location=len(priorities)-1
            # 찾으려는 수가 가장크면
            else:
                return count+1
        
        #그 이후 숫자면
        else:
            #맨앞의 숫자가 배열의 가장 큰 수보다 작으면
            if priorities[0]<max(priorities):
                #맨앞의 숫자를 뒤로보내고
                priorities.append(priorities.pop(0))
                #찾으려는 수의 인덱스를 앞으로 땡김
                location=-1
            #맨앞의 숫자가 배열의 가장 큰 수보다 크면
            else:
                #맨앞의 숫자 지우고
                priorities.pop(0)
                #찾으려는 인덱스 땡기고
                location=-1
                #프린트 순서 하나 더해줌
                count+=1
            
       
        
   
    
    return answer

solution(priorities, location)