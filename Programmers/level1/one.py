import re
'''
    s에는 사람 이름
    ,로 구분, 띄어쓰기로 구분
    if 미들네임 있다면
        두번째 인덱스 하나 가져와서 소문자로 넣어야함
        
    중복있을시 --> 숫자 붙여줘야함 
    정답 배열에 넣어줘야함
    
    c는 회사이름 -> 소문자
'''

S='John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, Jane Doe, Penny Parker'
C='Example'

def checkSet(email, nList):
    for i in nList:
        if email in nList:
            return 1
        else:
            return 0

def solution(S, C):
    C=C.lower()
    C='@'+C+'.com>'
    print(C)
    list=S.split(',')
    answer=[] #정답배열
    nList=[] #이메일 앞부분
    temp=[] #중복이름 넣어주는 배열
    final='' #최종 문자열

    for i in list:
        sList=i.split( )
        email=''
        name=''
        
        
        if len(sList) >2:
            '''
            email+=sList[0]+" "
            email+=sList[1]+" "
            email+=sList[2]+" "
            email+="<"
            '''
            name+=sList[0]+" "
            name+=sList[1]+" "
            name+=sList[2]+" "
            name+="<"
            print(name)
            email+=sList[0][0].lower()
            email+=sList[1][0].lower()
            email+=re.sub("-","",sList[2].lower())[0:8]
            bCheck=checkSet(email, nList)
            
            if bCheck == 1:
                temp.append(email)
                print(temp)
                email+=str(temp.count(email)+1)
            nList.append(email)
            answer.append(name+email+C)
            
        else:
            '''
            email+=sList[0]+" "
            email+=sList[1]+" "
            email+="<"
            '''
            name+=sList[0]+" "
            name+=sList[1]+" "
            name+="<"
            email+=sList[0][0].lower()
            email+=re.sub("-","",sList[1].lower())[0:8]
            bCheck=checkSet(email, nList)
            if bCheck == 1:
                temp.append(email)
                print(temp)
                email+=str(temp.count(email)+1)
            nList.append(email)
            answer.append(name+email+C)
            
    print(answer)
    final=", ".join(answer)
    print(final)
      
    
    return final
        
solution(S, C)

#중복있는지 체크해주는 메소드

    
        




















