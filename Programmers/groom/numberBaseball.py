import random

rn=["0","0","0"]
rn[0] = str(random.randrange(1, 9, 1))
rn[1] = rn[0]
rn[2] = rn[0]
while (rn[0] == rn[1]):
    rn[1] = str(random.randrange(1,9,1))
while (rn[0] == rn[2] or rn[1] == rn[2]):
    rn[2] = str(random.randrange(1,9,1))
    
def baseBall(com):
    count=0
    scount=0
    bcount=0
    
    
    while (scount < 3):
        
        num = str(input("숫자 3자리를 입력하세요 : "))
        
        scount=0
        bcount=0
        
        
        
        for i in range(0, 3):
            for j in range(0, 3):
                if(num[i] == str(rn[j]) and i == j):
                    scount+=1
                elif(num[i] == str(rn[j]) and i !=j ):
                    bcount+=1
        print(f"결과 : [{scount}] Strike [{bcount}] Ball")
        count+=1
    
    print("---------------")
    print(f"{count}번 만에 정답 맞춤")   
    
baseBall(rn)