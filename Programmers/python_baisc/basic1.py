import re

new_id="=.="


def solution(new_id):
    answer = ''
    #1단계
    new_id=new_id.lower()
    #2단계
    new_id=re.sub('[~!@#$%^&*\(\)=+\[\{\]\}:?,\<\>/]', '', new_id)
        
    #print(new_id)
    #3단계
    new_id=re.sub('\.+', '.', new_id)
    
    #4단계
    if len(new_id) > 0 :
        if new_id[0]==".":
            new_id=new_id[1:]
    if len(new_id) > 0 :  
        if new_id[-1]==".":
            new_id=new_id[:-1]
    
    #5단계
    if len(new_id) == 0:
            new_id="a"
    
    #6단계
    if len(new_id) > 15:
        new_id=new_id[:15]
        if new_id[-1] ==".":
            new_id=new_id[:-1]
    
    #7단계
    while len(new_id) < 3:
        new_id+=new_id[-1]
                             
            
    print(new_id,end="")
    answer=new_id
    return answer

#solution(new_id)


a='nct dream'
print(a[:-1])












